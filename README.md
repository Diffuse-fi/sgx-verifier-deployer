# SGX Verification Infrastructure Deployment

This repository contains scripts for Automata's SGX verification contracts deployment. These scripts ensure smooth deployment on multiple chains and are essential for continuous updates of our infrastructure.

## Overview
All scripts parse addresses as environment variables. Addresses are stored in addresses/chain_name/env_var_name.txt. So, if there are no contracts at all, like in a fresh local node, then deploy/script.py will deploy all contracts and will write addresses to appropriate .txt files. If there are some contracts, for example, the chain already has DAIMO_P256 and RISCZERO_VERIFIER deployed, but no automata contracts, then write addresses to the corresponding files which will be used in further steps. Here is a brief overview of the contracts: 


- **RIP7212_P256_PRECOMPILE** – Naive quote verification using secp256r1 signature verification. `P256Configuration.sol` checks if the precompile exists and uses it as a verifier. Some chains may have it but not at the 0x100 address. You have the opportunity to define a custom precompile address.
- **DAIMO_P256** – If there is no precompile then solidity implementation is used: [DAIMO P256 Verifier](https://github.com/daimo-eth/p256-verifier)
- **RISCZERO_VERIFIER** – Risc0 Groth16 verifier.


**On-chain PCCS** consists of helper contracts:
- **X509_HELPER**
- **X509_CRL_HELPER**
- **FMSPC_TCB_HELPER**
- **ENCLAVE_IDENTITY_HELPER**

... and `pccs` contracts themselves:
- **PCCS_STORAGE**
- **ENCLAVE_ID_DAO**
- **FMSPC_TCB_DAO**
- **PCK_DAO**
- **PCS_DAO**

**Dcap-attestation** contracts:
- **V4_VERIFIER**
- **V3_VERIFIER**
- **DCAP_ATTESTATION**
- **PCCS_ROUTER**

## Prerequisites
Infrastructure deployment consists of three steps:
1. Contracts deployment (`script/deploy.py`)
2. Upload of the certificates that `automata-dcap-qpl-tool` has not uploaded automatically (`script/upsert.py`)
3. Upload of the collaterals using `automata-dcap-qpl-tool` (`script/run_qpl_tool.py`)
Some chains may contain already deployed contracts (steps 1-2 done) but with outdated collaterals(step 3). The original `automata-dcap-qpl` repo contains hardcoded contract addresses and rpc_url and cannot be used on any chain out of the box. Our fork parses addresses and rpc_url as environment variables, so it can be used on any chain.

⚠️ IMPORTANT! ⚠️ You have to use `qpl-tool` with a quote from your machine, not an example quote! The tool will request collaterals from Intel's API for the CPU that created the quote and will upload them on chain. Then automata-dcap-zkvm-cli will parse data from the chain and will fail if there is no data for the target CPU. You will need to update the path to quote in `script/run_qpl_tool.py`

Scripts read addresses from `addresses/<chain-name>/<environment-variable-name>.txt`.
Add your chain to `script/utils/network.py and contract addresses to addresses/<chain-name>.txt`.
For example, a fresh local node with no contra will have no addresses in `addresses/local/`,
Some chain may contain p256-verifier and risc0-verifier, then there should be 2 files in `addresses/<chain-name>/`
If everything is deployed then you will need to place 15 files into the corresponding directory.

### Troubleshooting risc0 verifier
If there is no risc0 verifier presented on the destination chain, you need to deploy one.
release-1.1 produces seal that starts with `0x50bd1769`, 1.2 and 1.3 -- with `0xc101b42b`.
Looks like Bonsai works on 1.1, need to checkout to this branch.
Error in solidity for versions mismatch is "custom error 0xb8b38d4c".

### Troubleshooting SP1 verifier
SP1 verifier is not supported for now. Only the Risc0 verifier is used. This repository's scripts are intended to be used specifically with the Risc0 verifier. 

## Workflow
### Launch local node

To launch the contracts on a local node, you can use `anvil`:
```
anvil
```
and switch to another window.

### export env variables

Required rev variables are listed in `.env.example`, copy its contents to `.env` file:
```
cp .env.example .env
```
paste all needed information to `.env` file and read environment variables from it
```
source .env
```

### run deployment script
Build the `qpl` tool:
```
cd lib/automata-dcap-qpl/automata-dcap-qpl-tool
cargo build --release
```
... and run the deployment script:
```
python script/deploy_upsert_qpl.py
```

The expected result of the `automata-dcap-qpl-tool` run is
```missing_collateral: None```


### Great job!
SGX verification infrastructure should be ready to work now!
