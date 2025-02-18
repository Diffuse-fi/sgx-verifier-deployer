import subprocess
from utils.network import *

for network in networks:
    cmd = ['cast', 'gas-price', '--rpc-url=' + network.rpc_url]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("request succeeded")
        print(network.name, "gas price:", int(res.stdout.strip())/(10**9), "gwei")
    else:
        print("request failed")
        print(res)

