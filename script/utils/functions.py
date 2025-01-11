import os

def addr_filename(network, contract):
    return "addresses/" + network.dirname + contract.env_var_name + ".txt"

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

