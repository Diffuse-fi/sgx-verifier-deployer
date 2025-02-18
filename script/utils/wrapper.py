from dataclasses import dataclass

@dataclass(frozen=True)
class ContractWrapperClass:
    env_var_name: str
    script_contract_name: str
    default_method: str
    log_splitter: str
    root: str

ENCLAVE_IDENTITY_HELPER = ContractWrapperClass(
    env_var_name="ENCLAVE_IDENTITY_HELPER",
    script_contract_name="DeployHelpers",
    default_method="deployEnclaveIdentityHelper()",
    log_splitter="[LOG] EnclaveIdentityHelper:  ",
    root="lib/automata-on-chain-pccs/"
)
FMSPC_TCB_HELPER = ContractWrapperClass(
    env_var_name="FMSPC_TCB_HELPER",
    script_contract_name="DeployHelpers",
    default_method="deployFmspcTcbHelper()",
    log_splitter="[LOG] FmspcTcbHelper:  ",
    root="lib/automata-on-chain-pccs/"
)
X509_HELPER = ContractWrapperClass(
    env_var_name="X509_HELPER",
    script_contract_name="DeployHelpers",
    default_method="deployPckHelper()",
    log_splitter="[LOG] PCKHelper/X509Helper:  ",
    root="lib/automata-on-chain-pccs/"
)
X509_CRL_HELPER = ContractWrapperClass(
    env_var_name="X509_CRL_HELPER",
    script_contract_name="DeployHelpers",
    default_method="deployX509CrlHelper()",
    log_splitter="[LOG] X509CRLHelper:  ",
    root="lib/automata-on-chain-pccs/"
)
DEPLOY_AUTOMATA_DAO = ContractWrapperClass(
    env_var_name="",
    script_contract_name="DeployAutomataDao",
    default_method="deployAll(bool)",
    log_splitter="",
    root="lib/automata-on-chain-pccs/"
)
CONFIG_AUTOMATA_DAO = ContractWrapperClass(
    env_var_name="",
    script_contract_name="ConfigAutomataDao",
    default_method="updateStorageDao()",
    log_splitter="",
    root="lib/automata-on-chain-pccs/"
)


DAIMO_P256 = ContractWrapperClass(
    env_var_name="DAIMO_P256",
    script_contract_name="DeployScript",
    default_method="",
    log_splitter="new P256Verifier@",
    root="lib/p256-verifier"
)

RIP7212_P256_PRECOMPILE = ContractWrapperClass(
    env_var_name="RIP7212_P256_PRECOMPILE",
    script_contract_name="",
    default_method="",
    log_splitter="",
    root=""
)


PCCS_STORAGE = ContractWrapperClass(
    env_var_name="PCCS_STORAGE",
    script_contract_name="",
    default_method="",
    log_splitter="AutomataDaoStorage deployed at  ",
    root="lib/automata-on-chain-pccs/"
)

ENCLAVE_ID_DAO = ContractWrapperClass(
    env_var_name="ENCLAVE_ID_DAO",
    script_contract_name="",
    default_method="",
    log_splitter="AutomataEnclaveIdDao deployed at:  ",
    root="lib/automata-on-chain-pccs/"
)

FMSPC_TCB_DAO = ContractWrapperClass(
    env_var_name="FMSPC_TCB_DAO",
    script_contract_name="",
    default_method="",
    log_splitter="AutomataFmspcTcbDao deployed at:  ",
    root="lib/automata-on-chain-pccs/"
)

PCK_DAO = ContractWrapperClass(
    env_var_name="PCK_DAO",
    script_contract_name="",
    default_method="",
    log_splitter="AutomataPckDao deployed at:  ",
    root="lib/automata-on-chain-pccs/"
)

PCS_DAO = ContractWrapperClass(
    env_var_name="PCS_DAO",
    script_contract_name="",
    default_method="",
    log_splitter="AutomataPcsDao deployed at:  ",
    root="lib/automata-on-chain-pccs/"
)



PCCS_ROUTER = ContractWrapperClass(
    env_var_name="PCCS_ROUTER",
    script_contract_name="DeployRouter",
    default_method="",
    log_splitter="Deployed PCCSRouter to ",
    root="lib/automata-dcap-attestation/"
)
DCAP_ATTESTATION = ContractWrapperClass(
    env_var_name="DCAP_ATTESTATION",
    script_contract_name="AttestationScript",
    default_method="deployEntrypoint()",
    log_splitter="Automata Dcap Attestation deployed at:  ",
    root="lib/automata-dcap-attestation/"
)
V3_VERIFIER = ContractWrapperClass(
    env_var_name="V3_VERIFIER",
    script_contract_name="DeployV3",
    default_method="",
    log_splitter="V3QuoteVerifier deployed at  ",
    root="lib/automata-dcap-attestation/"
)
V4_VERIFIER = ContractWrapperClass(
    env_var_name="V4_VERIFIER",
    script_contract_name="DeployV4",
    default_method="",
    log_splitter="V4QuoteVerifier deployed at  ",
    root="lib/automata-dcap-attestation/"
)

pccs_helpers = [
    ENCLAVE_IDENTITY_HELPER,
    FMSPC_TCB_HELPER,
    X509_HELPER,
    X509_CRL_HELPER
]

automata_dao_contracts = [
    PCCS_STORAGE,
    ENCLAVE_ID_DAO,
    FMSPC_TCB_DAO,
    PCK_DAO,
    PCS_DAO
]

RISCZERO_VERIFIER = ContractWrapperClass(
    env_var_name="RISCZERO_VERIFIER",
    script_contract_name="lib/risc0-ethereum/contracts/script/DeployVerifier.s.sol",
    default_method="",
    log_splitter="Deployed RiscZeroGroth16Verifier to ",
    root=""
)