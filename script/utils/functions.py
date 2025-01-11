import os
from .wrapper import DEPLOY_AUTOMATA_DAO, automata_dao_contracts
from .config import BASE_DIR
def addr_filename(network, contract):
    return os.path.join(BASE_DIR, "addresses/" + network.dirname + contract.env_var_name + ".txt")

def parse_env_var(network, contract):
    with open(addr_filename(network, contract), 'r') as file:
        address = file.read().strip()
        os.environ[contract.env_var_name] = address

def extract_address_from_logs(log, network, contract):
    address = log.split(contract.log_splitter)[1].split('\n')[0]

    with open(addr_filename(network, contract), 'w') as file:
        file.write(address)

    parse_env_var(network, contract)

def form_command(contract, network, method=None, input=None):
    _command = [
        "forge",
        "script",
        "--root",
        contract.root,
        contract.script_contract_name,
        "--rpc-url=" + network.rpc_url,
        "-vvvv",
        "--broadcast"
    ]

    if contract.default_method != "":
        _command.append("--sig")
        if method == None:
            method = contract.default_method
        _command.append(method)

    if input is not None:
        _command.extend(input)

    return _command

def is_already_deployed(network, contract):
    if contract == DEPLOY_AUTOMATA_DAO:
        for c in automata_dao_contracts:
            if os.path.exists(addr_filename(network, c)):
                parse_env_var(network, c)
            else:
                return False
        print("automata_dao_contracts are alreary deployed, skipping")
        return True

    if os.path.exists(addr_filename(network, contract)):
        print(contract.env_var_name + " is alreary deployed, skipping")
        parse_env_var(network, contract)
        return True
    else:
        return False

