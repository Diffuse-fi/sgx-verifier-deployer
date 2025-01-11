from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkClass:
    dirname: str
    rpc_url: str


LOCAL = NetworkClass(
    dirname="local/",
    rpc_url="http://localhost:8545"
)
