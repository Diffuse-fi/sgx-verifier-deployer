# sgx_verification_infrastructure_deployer
Automate automata's contracts deployment

Welcome to the automated automata's verification infrastructure deployment repo. Guys have some awesome code but readmes lag behind the code. And even if readmes were relevant, there are 14 contracts involved that either need to be deployed or used in each other's configuration. Handling all of this is huge pain in the head, especially if you want to work on more than one chain.

## Overwiev
All scripts parse addresses as environment variables. They are stored in addresses/chain_name/env_var_name.txt. So, if there are no contracts at all, like in a fresh local node, then deploy/script.py will deploy all contracts and will write addresses to appropriate .txt files. If there are some contracts, for example, chain already has DAIMO_P256 and RISCZERO_VERIFIER deployed, but no automata contracts, then write addresses to corresponding .txt files and they will be used in further steps. Here is brief overwiew of what every contract is


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


## Workflow
### Launch local node
If want to work on a local node, launch anvil
```
anvil
```
and switch to other window.

### export env variables
Create directory for addresses. For local it will be
```
mkdir addresses/local/
```

### export env variables
Required rev variables are listed in .env.example, copy its contents to .env file:
```
cp .env.example .env
```
paste all needed information to .env file and read environment variables from it
```
source .env
```

### build and test
next build and test on-chain-pccs
```
forge build --root lib/automata-on-chain-pccs/
forge test --root lib/automata-on-chain-pccs/
```
dcap-attestation

```
forge build --root lib/automata-dcap-attestation/
export DCAP_RISCZERO_IMAGE_ID=0x83613a8beec226d1f29714530f1df791fa16c2c4dfcf22c50ab7edac59ca637f
forge test --root lib/automata-dcap-attestation/
```

### deploy risc0 verifier
Place risc0 groth16 verifier address to addresses/<your-chain>/RISCZERO_VERIFIER.txt if it is already deployed on your chain.
If not, our script will deploy it for you, but furst you will need to run build script:
```
python3 script/build_risc_foundry_template.py
```
and write RiscZeroGroth16Verifier address fto addresses/<your-chain>/RISCZERO_VERIFIER.txt

### SP1 verifier
is not supported, we use risc0 and I slipped everything related to sp1

### run deployment script
Place P256 verifier address to addresses/<your-chain>/DAIMO_P256.txt if it is already deployed on your chain (or script will deploy it new one). Run script:
```
python script/deploy.py
```
it will deploy all needed contracts and write addresses to addresses/<your-chain>/ dir.

### run deployment script
Upload certificates to PCS_DAO:
```
python script/upsert.py
```

### run deployment script
Use qpl tool to update missing collaterals:
```
cd lib/automata-dcap-qpl/automata-dcap-qpl-tool
cargo build --release
./target/release/automata-dcap-qpl-tool --quote_file=../../automata-dcap-zkvm-cli/data/quote.hex --private_key=$PRIVATE_KEY
#TODO here we will need to pass rpc url and other stuff that is hardcoded now
# maybe should wrap into cli
```
Maybe you will need to run it several times if I remover loop from it. Desired result is
```missing_collateral: None```

**IMPORTANT!** You have to use qpl-tool with quote from your machine, not an example quote! Tool will request collaterals from intel's API for cpu that created the quote and will upload them to the to chain. Then automata-dcap-zkvm-cli will parse data from chain and will fail if there are no data for you cpu.

### Great job!
Sgx verification infrastructure should be ready to work now! You can try to use automata-dcap-zkvm-cli, journal and seal verification should succeed.
