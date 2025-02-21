import subprocess
import os
import argparse
from utils.functions import parse_env_var
from utils.network import *
from utils.wrapper import PCCS_STORAGE, automata_dao_contracts

os.environ["PRIVATE_KEY"] = os.getenv("PRIVATE_KEY")

def run_qpl_tool(network):

    os.environ["RPC_URL"] = network.rpc_url

    for automata_dao_contract in automata_dao_contracts:
        if automata_dao_contract == PCCS_STORAGE:
            continue
        parse_env_var(network, automata_dao_contract)

    cmd = [
        './lib/automata-dcap-qpl/automata-dcap-qpl-tool/target/release/automata-dcap-qpl-tool',
        '--quote_file',
        '../../cli/test_data/0/sgx_quote.bin',
        '--chain_id=' + network.chain_id,
        '--rpc_url=' + network.rpc_url,
        '--private_key=' + os.getenv("PRIVATE_KEY")
    ]
    print(cmd)
    subprocess.run(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data feeder parameters")
    parser.add_argument('-n', '--network', type=network_class, required=True, help="Choose network")
    args = parser.parse_args()

    run_qpl_tool(args.network)