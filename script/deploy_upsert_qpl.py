import argparse
from deploy import deploy
from upsert import upsert
from run_qpl_tool import run_qpl_tool
from utils.network import *

def main(network):
    deploy(network)
    upsert(network)
    run_qpl_tool(network)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data feeder parameters")
    parser.add_argument('-n', '--network', type=network_class, required=True, help="Choose network")
    args = parser.parse_args()

    main(args.network)