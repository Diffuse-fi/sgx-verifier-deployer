from datetime import datetime
import subprocess
import os
import sys
import argparse
from utils.functions import is_already_deployed, parse_env_var, extract_address_from_logs, form_command
from utils.special_checks import special_check
from utils.network import *
from utils.wrapper import pccs_helpers
from utils.wrapper import automata_dao_contracts
from utils.wrapper import DAIMO_P256, RIP7212_P256_PRECOMPILE
from utils.wrapper import DEPLOY_AUTOMATA_DAO, CONFIG_AUTOMATA_DAO
from utils.wrapper import PCCS_ROUTER, DCAP_ATTESTATION, V3_VERIFIER, V4_VERIFIER
from utils.wrapper import RISCZERO_VERIFIER


def call_script(network, contract, method=None, input=None):

    print(contract.script_contract_name, method if method is not None else contract.default_method, end="...\n")

    _command = form_command(contract, network, method, input)

    result = subprocess.run(_command, capture_output=True, text=True)

    with open(logs_path, 'a') as logs:
        logs.write(str(_command))
        logs.write("\nstderr:\n")
        logs.write(result.stderr)
        logs.write("\nstdout:\n")
        logs.write(result.stdout)
        logs.write("\n========================================\n")

    if result.returncode != 0:
        print("subprocess run unsuccessful!")
        sys.exit(1)

    return (result.stdout)


def deploy_contract(network, contract, method=None, input=None):

    print("deploying " + contract.script_contract_name + "... ", end ="")

    if contract.env_var_name != "" or contract == DEPLOY_AUTOMATA_DAO:
        if is_already_deployed(network, contract) == True:
            return

    log = call_script(network, contract, method, input)

    if contract != DEPLOY_AUTOMATA_DAO:
        extract_address_from_logs(log, network, contract)
    else:
        for s in automata_dao_contracts:
            extract_address_from_logs(log, network, s)

    print("success!")




current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)
logs_path = os.path.join(logs_dir, current_time + ".txt")
with open(logs_path, "w") as file:
    file.write(current_time + "\n")

def deploy(network):

    special_check(network)

    print("writing logs to", logs_path)

    os.environ["RPC_URL"] = network.rpc_url
    os.environ["PRIVATE_KEY"] = os.getenv("PRIVATE_KEY")

    # steps from https://github.com/automata-network/automata-on-chain-pccs
    for pccs_helper in pccs_helpers:
        deploy_contract(network, pccs_helper)

    # 2 steps not from on-chain-pccs, because they are hardcoded in original automata repo
    #TODO: don't need to deploy if RIP7212_P256_PRECOMPILE, not handled now and deploys in any case
    deploy_contract(network, DAIMO_P256, input=["--private-key", os.getenv("PRIVATE_KEY")])
    os.environ["RIP7212_P256_PRECOMPILE"] = '0x0000000000000000000000000000000000000100'

    deploy_contract(network, DEPLOY_AUTOMATA_DAO, input=["true"])
    call_script(network, CONFIG_AUTOMATA_DAO)

    # steps from https://github.com/automata-network/automata-dcap-attestation
    deploy_contract(network, PCCS_ROUTER)
    deploy_contract(network, DCAP_ATTESTATION)

    deploy_contract(network, V3_VERIFIER)
    call_script(network, DCAP_ATTESTATION, method="configVerifier(address)", input=[os.getenv("V3_VERIFIER")])

    deploy_contract(network, V4_VERIFIER)
    call_script(network, DCAP_ATTESTATION, method="configVerifier(address)", input=[os.getenv("V4_VERIFIER")])

    ImageID = "83613a8beec226d1f29714530f1df791fa16c2c4dfcf22c50ab7edac59ca637f"
    deploy_contract(network, RISCZERO_VERIFIER)
    call_script(
        network,
        DCAP_ATTESTATION,
        method="configureZk(uint8 zk, address verifierGateway, bytes32 programId)",
        input=["1", os.getenv("RISCZERO_VERIFIER"), ImageID]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data feeder parameters")
    parser.add_argument('-n', '--network', type=network_class, required=True, help="Choose network")
    args = parser.parse_args()

    deploy(args.network)