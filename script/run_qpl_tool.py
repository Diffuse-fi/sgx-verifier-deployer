import subprocess
import os
from utils.functions import parse_env_var
from utils.network import LOCAL_NETWORK
from utils.wrapper import automata_dao_contracts

os.environ["PRIVATE_KEY"] = os.getenv("PRIVATE_KEY")

def run_qpl_tool(network):

    os.environ["RPC_URL"] = network.rpc_url

    for automata_dao_contract in automata_dao_contracts:
        parse_env_var(network, automata_dao_contract)

    subprocess.run(
        [
            './lib/automata-dcap-qpl/automata-dcap-qpl-tool/target/release/automata-dcap-qpl-tool',
            '--quote_file',
            '../../cli/test_data/0/sgx_quote.bin',
            '--private_key=' + os.getenv("PRIVATE_KEY")

        ]
    )


if __name__ == "__main__":
    run_qpl_tool(LOCAL_NETWORK)