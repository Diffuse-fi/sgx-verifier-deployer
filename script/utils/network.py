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


LOCAL_NETWORK = NetworkClass(
    name="local",
    dirname = "local/",
    rpc_url="http://localhost:1488",
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

TAIKO_MAINNET = NetworkClass(
    name="taiko_mainnet",
    dirname = "taiko_mainnet/",
    rpc_url="https://rpc.mainnet.taiko.xyz",
    chain_id="167000"
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

BSC_MAINNET = NetworkClass( # binance smart chain
    name="bsc_mainnet",
    dirname = "bsc_mainnet/",
    rpc_url="https://bsc-dataseed.binance.org/",
    chain_id="56"
)

POLYGON_MAINNET = NetworkClass(
    name="polygon_mainnet",
    dirname = "polygon_mainnet/",
    rpc_url="https://polygon-rpc.com/",
    chain_id="137"
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
    rpc_url="https://optimism.rpc.subquery.network/public",
    chain_id="10"
)

HARMONY_MAINNET = NetworkClass(
    name="harmony_mainnet",
    dirname = "harmony_mainnet/",
    rpc_url="https://api.harmony.one",
    chain_id="1666600000"
)

MOONBEAM_MAINNET = NetworkClass(
    name="moonbeam_mainnet",
    dirname = "moonbeam_mainnet/",
    rpc_url="https://rpc.api.moonbeam.network",
    chain_id="1666600000"
)

CRONOS_MAINNET = NetworkClass(
    name="cronos_mainnet",
    dirname = "cronos_mainnet/",
    rpc_url="https://evm.cronos.org",
    chain_id="25"
)

BASE_MAINNET = NetworkClass(
    name="base_mainnet",
    dirname = "base_mainnet/",
    rpc_url="https://mainnet.base.org",
    chain_id="8453"
)

ZKSYNC_MAINNET = NetworkClass(
    name="zksync_mainnet",
    dirname = "zksync_mainnet/",
    rpc_url="https://mainnet.era.zksync.io ",
    chain_id="324"
)

WORLD_MAINNET = NetworkClass(
    name="world_mainnet",
    dirname = "world_mainnet/",
    rpc_url="https://worldchain-mainnet.g.alchemy.com/public",
    chain_id="480"
)

ZORA_MAINNET = NetworkClass(
    name="zora_mainnet",
    dirname = "zora_mainnet/",
    rpc_url="https://rpc.zora.energy",
    chain_id="7777777"
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

ZIRCUIT_MAINNET = NetworkClass(
    name="zircuit_mainnet",
    dirname = "zircuit_mainnet/",
    rpc_url="https://mainnet.zircuit.com",
    chain_id="48900"
)

MANTLE_MAINNET = NetworkClass(
    name="mantle_mainnet",
    dirname = "mantle_mainnet/",
    rpc_url="https://rpc.mantle.xyz",
    chain_id="5000"
)



networks = [
    LOCAL_NETWORK,
    NEON_DEVNET,
    ETH_SEPOLIA,
    TAIKO_HEKLA,
    ASSET_TESTNET,
    MONAD_TESTNET,
    BSC_MAINNET,
    POLYGON_MAINNET,
    AVAX_MAINNET,
    SONIC_MAINNET,
    ARBITRUM_MAINNET,
    OPTIMISM_MAINNET,
    HARMONY_MAINNET,
    CRONOS_MAINNET,
    BASE_MAINNET,
    ZKSYNC_MAINNET,
    WORLD_MAINNET,
    ZORA_MAINNET,
    ATA_MAINNET,
    TAIKO_MAINNET,
    BERACHAIN_MAINNET,
    ZIRCUIT_MAINNET,
    MANTLE_MAINNET,
    ETH_MAINNET
]

def network_class(name):
    for n in networks:
        if n.name == name:
            return n
    print("network with", name, "name is not found!")
    sys.exit(1)

