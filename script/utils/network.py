from dataclasses import dataclass
import os
import sys

@dataclass(frozen=True)
class NetworkClass:
    name: str
    dirname: str
    rpc_url: str
    chain_id: str

alchemy_api_key = os.getenv('ALCHEMY_API_KEY')
monad_api_key = os.getenv('MONAD_API_KEY')


LOCAL_NETWORK = NetworkClass(
    name="local",
    dirname = "local/",
    rpc_url="http://localhost:8545",
    chain_id="31337"
)

NEON_DEVNET = NetworkClass(
    name="neon_devnet",
    dirname = "neon_devnet/",
    rpc_url="https://devnet.neonevm.org",
    chain_id="245022926"
)

ETH_SEPOLIA = NetworkClass(
    name="eth_sepolia",
    dirname = "eth_sepolia/",
    rpc_url="https://eth-sepolia.g.alchemy.com/v2/" + alchemy_api_key,
    chain_id="11155111"
)

ETH_MAINNET = NetworkClass(
    name="eth_mainnet",
    dirname = "eth_mainnet/",
    rpc_url="https://eth-mainnet.g.alchemy.com/v2/" + alchemy_api_key,
    chain_id="1"
)

TAIKO_HEKLA = NetworkClass(
    name="taiko_hekla",
    dirname = "taiko_hekla/",
    rpc_url="https://rpc.hekla.taiko.xyz",
    chain_id="167009"
)

ARTHERA_TESTNET = NetworkClass(
    name="arthera_testnet",
    dirname = "arthera_testnet/",
    rpc_url="https://rpc-test.arthera.net",
    chain_id="10243"
)

MONAD_TESTNET = NetworkClass(
    name="monad_testnet",
    dirname = "monad_testnet/",
    rpc_url="https://rpc-testnet.monadinfra.com/rpc/" + monad_api_key,
    chain_id="10143"
)


networks = [
    LOCAL_NETWORK,
    NEON_DEVNET,
    ETH_SEPOLIA,
    TAIKO_HEKLA,
    ARTHERA_TESTNET,
    MONAD_TESTNET,
    ETH_MAINNET
]

def network_class(name):
    for n in networks:
        if n.name == name:
            return n
    print("network with", name, "name is not found!")
    sys.exit(1)

