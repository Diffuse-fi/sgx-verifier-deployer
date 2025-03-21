from web3 import Web3
import os
from utils.network import *
from utils.functions import parse_env_var
from utils.wrapper import FMSPC_TCB_DAO, ENCLAVE_ID_DAO
import argparse
import json

def upsert_fmspc_dao(network):
    RPC_URL = network.rpc_url
    parse_env_var(network, FMSPC_TCB_DAO)

    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.is_connected():
        raise Exception("RPC connection error")

    # FMSPC contract ABI
    with open("lib/automata-on-chain-pccs/js/tcbinfo/abi/FmspcTcbDao.json", "r") as file:
        data = json.load(file)
        ABI = data["abi"]

    contract = web3.eth.contract(os.getenv("FMSPC_TCB_DAO"), abi=ABI)

    # tx input from qpl-tool
    with open("script/collaterals/tcbInfo/object", 'r') as file:
        object = file.read()

    with open("script/collaterals/tcbInfo/signature", 'r') as file:
        signature = file.read()

    tcb_info = (
        object,
        web3.to_bytes(hexstr=signature)
    )

    # abi encoding
    method = contract.functions.upsertFmspcTcb(tcb_info)
    encoded_data = method._encode_transaction_data()
    common_part(network, web3, encoded_data, os.getenv("FMSPC_TCB_DAO"))


def upsert_enclave_identity(network):
    RPC_URL = network.rpc_url
    parse_env_var(network, ENCLAVE_ID_DAO)

    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.is_connected():
        raise Exception("RPC connection error")

    # EnclaveIdentityDao contract ABI
    # upsertEnclaveIdentity(uint256 id, uint256 version, EnclaveIdentityJsonObj calldata enclaveIdentityObj) external returns (bytes32 attestationId)
    with open("lib/automata-on-chain-pccs/js/identity/abi/EnclaveIdentityDao.json", "r") as file:
        data = json.load(file)
        ABI = data["abi"]

    contract = web3.eth.contract(os.getenv("ENCLAVE_ID_DAO"), abi=ABI)

    # tx input from qpl-tool
    with open("script/collaterals/enclaveIdentity/object", 'r') as file:
        object = file.read()

    with open("script/collaterals/enclaveIdentity/signature", 'r') as file:
        signature = file.read()

    enclave_identity_json_obj = (
        object,
        web3.to_bytes(hexstr=signature)
    )

    # abi encoding
    method = contract.functions.upsertEnclaveIdentity(0, 3, enclave_identity_json_obj)
    encoded_data = method._encode_transaction_data()

    common_part(network, web3, encoded_data, os.getenv("ENCLAVE_ID_DAO"))


def common_part(network, web3, encoded_data, recepient):

    # print(f"ABI-Encoded Data: {encoded_data}")

    current_gas_price = web3.eth.gas_price
    print("current", network.name, "gas price:", current_gas_price / (10**9), "gwei")

    txn_data = {
        "from": os.getenv("PUBLIC_KEY"),
        "to": recepient,
        "gas": 10000000,
        "gasPrice": current_gas_price,
        "nonce": web3.eth.get_transaction_count(os.getenv("PUBLIC_KEY")),
        "chainId": int(network.chain_id),
        "data": encoded_data,
    }

    # sign and send tx
    signed_txn = web3.eth.account.sign_transaction(txn_data, os.getenv("PRIVATE_KEY"))

    try:
        web3.eth.call(txn_data)
    except Exception as e:
        print("Revert reason:", e)
        sys.exit(1)


    txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"Transaction sent: {txn_hash.hex()}")

    # wait for confirmation
    receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    if receipt.status != 1:
        print("FAILED!")
        sys.exit(1)
    else:
        print(f"Transaction confirmed! Hash: {txn_hash.hex()}")


def upsert_collaterals(network):
    upsert_fmspc_dao(network)
    upsert_enclave_identity(network)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data feeder parameters")
    parser.add_argument('-n', '--network', type=network_class, required=True, help="Choose network")
    args = parser.parse_args()

    upsert_collaterals(args.network)
