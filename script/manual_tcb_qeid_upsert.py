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
    tcb_info = (
        '{"version":2,"issueDate":"2025-03-12T20:36:57Z","nextUpdate":"2025-04-11T20:36:57Z","fmspc":"00606a000000","pceId":"0000","tcbType":0,"tcbEvaluationDataNumber":17,"tcbLevels":[{"tcb":{"sgxtcbcomp01svn":14,"sgxtcbcomp02svn":14,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":1,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2024-03-13T00:00:00Z","tcbStatus":"SWHardeningNeeded"},{"tcb":{"sgxtcbcomp01svn":14,"sgxtcbcomp02svn":14,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2024-03-13T00:00:00Z","tcbStatus":"ConfigurationAndSWHardeningNeeded"},{"tcb":{"sgxtcbcomp01svn":12,"sgxtcbcomp02svn":12,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":1,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2023-08-09T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"sgxtcbcomp01svn":12,"sgxtcbcomp02svn":12,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2023-08-09T00:00:00Z","tcbStatus":"OutOfDateConfigurationNeeded"},{"tcb":{"sgxtcbcomp01svn":11,"sgxtcbcomp02svn":11,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":1,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2023-02-15T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"sgxtcbcomp01svn":11,"sgxtcbcomp02svn":11,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2023-02-15T00:00:00Z","tcbStatus":"OutOfDateConfigurationNeeded"},{"tcb":{"sgxtcbcomp01svn":7,"sgxtcbcomp02svn":9,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":1,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2022-08-10T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"sgxtcbcomp01svn":7,"sgxtcbcomp02svn":9,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":13},"tcbDate":"2022-08-10T00:00:00Z","tcbStatus":"OutOfDateConfigurationNeeded"},{"tcb":{"sgxtcbcomp01svn":4,"sgxtcbcomp02svn":4,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":11},"tcbDate":"2021-11-10T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"sgxtcbcomp01svn":4,"sgxtcbcomp02svn":4,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":10},"tcbDate":"2020-11-11T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"sgxtcbcomp01svn":4,"sgxtcbcomp02svn":4,"sgxtcbcomp03svn":3,"sgxtcbcomp04svn":3,"sgxtcbcomp05svn":255,"sgxtcbcomp06svn":255,"sgxtcbcomp07svn":0,"sgxtcbcomp08svn":0,"sgxtcbcomp09svn":0,"sgxtcbcomp10svn":0,"sgxtcbcomp11svn":0,"sgxtcbcomp12svn":0,"sgxtcbcomp13svn":0,"sgxtcbcomp14svn":0,"sgxtcbcomp15svn":0,"sgxtcbcomp16svn":0,"pcesvn":5},"tcbDate":"2018-01-04T00:00:00Z","tcbStatus":"OutOfDate"}]}',
        web3.to_bytes(hexstr="0xd51bad8908fa4261d94b2a32bdb5e1ea00d241d6d50132d2087fef62cf7ea4ad07042a3ccfbd0ea55d5c10bbc37b5165c0fb3301f002b898b00ccb4a1797ab71")  # signature
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
    enclave_identity_json_obj = (
        '{"id":"QE","version":2,"issueDate":"2025-03-12T17:30:38Z","nextUpdate":"2025-04-11T17:30:38Z","tcbEvaluationDataNumber":17,"miscselect":"00000000","miscselectMask":"FFFFFFFF","attributes":"11000000000000000000000000000000","attributesMask":"FBFFFFFFFFFFFFFF0000000000000000","mrsigner":"8C4F5775D796503E96137F77C68A829A0056AC8DED70140B081B094490C57BFF","isvprodid":1,"tcbLevels":[{"tcb":{"isvsvn":8},"tcbDate":"2024-03-13T00:00:00Z","tcbStatus":"UpToDate"},{"tcb":{"isvsvn":6},"tcbDate":"2021-11-10T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"isvsvn":5},"tcbDate":"2020-11-11T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"isvsvn":4},"tcbDate":"2019-11-13T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"isvsvn":2},"tcbDate":"2019-05-15T00:00:00Z","tcbStatus":"OutOfDate"},{"tcb":{"isvsvn":1},"tcbDate":"2018-08-15T00:00:00Z","tcbStatus":"OutOfDate"}]}',
        web3.to_bytes(hexstr="0x09b6256751c46ad3e09dcb37318db32a18f9e741926ef596d646a7ffa5437a6893f06d0ce077e310ae78ce8b24a3c5229714f71711fb5cd27e8bb575cbaf32ef")  # signature
    )

    # abi encoding
    method = contract.functions.upsertEnclaveIdentity(0, 3, enclave_identity_json_obj)
    encoded_data = method._encode_transaction_data()

    common_part(network, web3, encoded_data, os.getenv("ENCLAVE_ID_DAO"))


def common_part(network, web3, encoded_data, recepient):

    # print(f"ABI-Encoded Data: {encoded_data}")

    max_priority_fee = web3.to_wei(10, "gwei")

    txn_data = {
        "from": os.getenv("PUBLIC_KEY"),
        "to": recepient,
        "gas": 10000000,
        "maxFeePerGas": web3.to_wei(10, "gwei"),
        "maxPriorityFeePerGas": max_priority_fee,
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
