import sys
from .network import ASSET_TESTNET

def asset_chain_config_check(network):
    if network == ASSET_TESTNET:
        print("asset chain does not support opcodes introduced in solidity 0.8.20")
        print("you need to change evm_version to \"paris\" is lib/p256-verifier/foundry.toml")
        print("and switch lib/risc0-ethereum submodule to")
        print("https://github.com/Diffuse-fi/risc0-ethereum/tree/release-1.3-asset-chain")
        while(True):
            user_input = input("If you haven't done it yet, do it and launch this script again. Resume? [y/n]: ").lower()
            if user_input == 'y':
                break
            elif user_input == 'n':
                print("cancelled execution", file=sys.stderr)
                sys.exit(1)
            else:
                print("Please enter 'y' or 'n'.")
                continue
