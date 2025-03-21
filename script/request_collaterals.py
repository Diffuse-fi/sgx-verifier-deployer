import requests


def request_tcb_info():
    pccs_url = "https://api.trustedservices.intel.com"
    collateral_version = "v3"
    tcb_type = "sgx"
    fmspc="00606a000000"

    req_url = f"{pccs_url}/{tcb_type}/certification/{collateral_version}/tcb?fmspc={fmspc}"

    process_request("tcbInfo", req_url)


def request_qeid():

    pccs_url = "https://api.trustedservices.intel.com"
    collateral_version = "v3"
    enclave_id_type = "sgx"

    req_url = f"{pccs_url}/{enclave_id_type}/certification/{collateral_version}/qe/identity"

    process_request("enclaveIdentity", req_url)


def process_request(collateral, req_url):
    print("requesting", req_url)
    response = requests.get(req_url)
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code} - {response.text}")

    data = response.text

    object = data.split(collateral + '":')[1].split(',"signature":"')[0]
    signature = data.split(',"signature":"')[1].split('"}')[0]

    with open("script/collaterals/" + collateral + "/object", 'w') as file:
        file.write(object)

    with open("script/collaterals/" + collateral + "/signature", 'w') as file:
        file.write(signature)
    print("wrote collateral to", "script/collaterals/" + collateral)


def request_collaterals():
      request_qeid()
      request_tcb_info()


if __name__ == "__main__":
    request_collaterals()
