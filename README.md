# sgx_verification_infrastructure_deployer
Automate automata's contracts deployment

Welcome to the automated automata's verification infrastructure deployment repo. Guys have some awesome code but readmes lag behind the code. And even if readmes were relevant, there are 14 contracts involved that either need to be deployed or used in each other's configuration. Handling all of this is huge pain in the head, especially if you want to work on more than one chain.

## Overwiev
All scripts parse addresses as environment variables. Addresses are stored in addresses/chain_name/env_var_name.txt. So, if there are no contracts at all, like in a fresh local node, then deploy/script.py will deploy all contracts and will write addresses to appropriate .txt files. If there are some contracts, for example, chain already has DAIMO_P256 and RISCZERO_VERIFIER deployed, but no automata contracts, then write addresses to corresponding .txt files and they will be used in further steps. Here is brief overwiew of what every contract is


- **RIP7212_P256_PRECOMPILE** – Naive quote verification using secp256r1 signature verification. `P256Configuration.sol` checks if the precompile exists and uses it as a verifier. Some chains may have it but not at the 0x100 address. Ypu have opportunity to define costom precompile address.
- **DAIMO_P256** – If there is no precompile then solidity implementation is used: [DAIMO P256 Verifier](https://github.com/daimo-eth/p256-verifier)
- **RISCZERO_VERIFIER** – Risc0 Groth16 verifier.


**On-chain PCCS** consists of helper contracts:
- **X509_HELPER**
- **X509_CRL_HELPER**
- **FMSPC_TCB_HELPER**
- **ENCLAVE_IDENTITY_HELPER**

and pccs contracts themselves:
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
1. deploy contracts (script/deploy.py)
2. upload certificates that automata-dcap-qpl-tool does not upload (script/upsert.py)
3. upload collaterals using automata-dcap-qpl-tool (script/run_qpl_tool.py)
Some chains may contain already deployed contracts (steps 1-2 done) but with outdated collaterals(step 3). Original automata-dcap-qpl repo contains hardcoded contrct addresses and rpc_url and cannot be used on any chain out-of-the-box, our fork parses addresses and rpc_url as environment variables, so it can be usen on any chain.

**IMPORTANT!** You have to use qpl-tool with quote from your machine, not an example quote! Tool will request collaterals from intel's API for cpu that created the quote and will upload them to the to chain. Then automata-dcap-zkvm-cli will parse data from chain and will fail if there are no data for you cpu. You will need to update path to quote in script/run_qpl_tool.py

Scripts read addresses from addresses/<chain-name>/<environment-variable-name>.txt.
Add your chain to script/utils/network.py and contract addresses to addresses/<chain-name>.txt.
For example, fresh local node with no contra will have no addresses in addresses/local/ ,
Some chain may contain p256-verifier and risc0-verifier, then there should be 2 files in addresses/<chain-name>/
And if you everything is deployed then you will need place 15 file to the corresponding directory.

### risc0 verifier
deploy risc0 verifier if your chain does not have in yet
release-1.1 produces seal that starts with 0x50bd1769, 1.2 and 1.3 -- with 0xc101b42b.
Looks like bonsai works on 1.1, need to checkout to this branch.
Error in solidity for versions mismatch is "custom error 0xb8b38d4c".

### SP1 verifier
is not supported, we use risc0 and I skipped everything related to sp1

## Workflow
### Launch local node
If want to work on a local node, launch anvil
```
anvil
```
and switch to other window.

### export env variables
Required rev variables are listed in .env.example, copy its contents to .env file:
```
cp .env.example .env
```
paste all needed information to .env file and read environment variables from it
```
source .env
```

### run deployment script
build qpl tool
```
cd lib/automata-dcap-qpl/automata-dcap-qpl-tool
cargo build --release
```
and run deployment script
```
python script/deploy_upsert_qpl.py
```

Expected result of automata-dcap-qpl-tool run is
```missing_collateral: None```


### Great job!
Sgx verification infrastructure should be ready to work now!
