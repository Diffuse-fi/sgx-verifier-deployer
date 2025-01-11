from deploy import deploy
from upsert import upsert
from run_qpl_tool import run_qpl_tool
from utils.network import LOCAL_NETWORK

def main(network):
    deploy(network)
    upsert(network)
    run_qpl_tool(network)

main(LOCAL_NETWORK)