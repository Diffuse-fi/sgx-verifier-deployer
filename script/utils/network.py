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
anvil_port = os.getenv('ANVIL_PORT')
anvil_port_2 = os.getenv('ANVIL_PORT_2')


LOCAL_NETWORK = NetworkClass(
    name="local",
    dirname = "local/",
    rpc_url="http://localhost:" + anvil_port,
    chain_id="31337"
)

LOCAL_NETWORK_2 = NetworkClass(
    name="local_2",
    dirname = "local_2/",
    rpc_url="http://localhost:" + anvil_port_2,
    chain_id="31337"
)

ETH_SEPOLIA = NetworkClass(
    name="eth_sepolia",
    dirname = "eth_sepolia/",
    rpc_url="https://eth-sepolia.g.alchemy.com/v2/" + alchemy_api_key,
    chain_id="11155111"
)

ETH_HOLESKY = NetworkClass(
    name="eth_holesky",
    dirname = "eth_holesky/",
    rpc_url="https://eth-holesky.g.alchemy.com/v2/" + alchemy_api_key,
    chain_id="11155111"
)

ASSET_TESTNET = NetworkClass(
    name="asset_testnet",
    dirname = "asset_testnet/",
    rpc_url="https://enugu-rpc.assetchain.org/",
    chain_id="42421"
)

MONAD_TESTNET = NetworkClass(
    name="monad_testnet",
    dirname = "monad_testnet/",
    rpc_url="https://testnet-rpc.monad.xyz/",
    chain_id="10143"
)

AVAX_MAINNET = NetworkClass( # avalanche c-net
    name="avax_mainnet",
    dirname = "avax_mainnet/",
    rpc_url="https://api.avax.network/ext/bc/C/rpc",
    chain_id="43114"
)

SONIC_MAINNET = NetworkClass(
    name="sonic_mainnet",
    dirname = "sonic_mainnet/",
    rpc_url="https://rpc.soniclabs.com",
    chain_id="146"
)

ARBITRUM_MAINNET = NetworkClass(
    name="arbitrum_mainnet",
    dirname = "arbitrum_mainnet/",
    rpc_url="https://arb1.arbitrum.io/rpc",
    chain_id="42161"
)

OPTIMISM_MAINNET = NetworkClass(
    name="optimism_mainnet",
    dirname = "optimism_mainnet/",
    rpc_url="https://opt-mainnet.g.alchemy.com/v2/" + alchemy_api_key,
    chain_id="10"
)

BASE_MAINNET = NetworkClass(
    name="base_mainnet",
    dirname = "base_mainnet/",
    rpc_url="https://mainnet.base.org",
    chain_id="8453"
)

ATA_MAINNET = NetworkClass(
    name="ata_mainnet",
    dirname = "ata_mainnet/",
    rpc_url="https://rpc.ata.network",
    chain_id="65536"
)

BERACHAIN_MAINNET = NetworkClass(
    name="bera_mainnet",
    dirname = "bera_mainnet/",
    rpc_url="https://rpc.berachain.com/",
    chain_id="80094"
)

MANTLE_MAINNET = NetworkClass(
    name="mantle_mainnet",
    dirname = "mantle_mainnet/",
    rpc_url="https://rpc.mantle.xyz",
    chain_id="5000"
)


networks = [
    LOCAL_NETWORK,
    LOCAL_NETWORK_2,
    ETH_SEPOLIA,
    ETH_HOLESKY,
    ASSET_TESTNET,
    MONAD_TESTNET,
    AVAX_MAINNET,
    SONIC_MAINNET,
    ARBITRUM_MAINNET,
    OPTIMISM_MAINNET,
    BASE_MAINNET,
    ATA_MAINNET,
    BERACHAIN_MAINNET,
    MANTLE_MAINNET,
]

networks_str = networks[0].name
for n in networks:
    if n==networks[0]:
        continue
    networks_str = networks_str + ", " + n.name


def network_class(name):
    for n in networks:
        if n.name == name:
            return n
    print("network with", name, "name is not found!")
    sys.exit(1)

