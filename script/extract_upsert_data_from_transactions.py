import json
import os

# for address PCS_DAO=0xcf171ACd6c0a776f9d3E1F6Cac8067c982Ac6Ce1:
# curl -X 'GET'   'https://automata-testnet-explorer.alt.technology/api/v2/addresses/0xcf171ACd6c0a776f9d3E1F6Cac8067c982Ac6Ce1/transactions'   -H 'accept: application/json' > script/json_transactions.json
file_path = 'script/json_transactions.json'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
else:
    print(f"file {file_path} not found")

count = 0
for item in data.get("items", []):

    decoded_input = item.get("decoded_input")
    method_call = decoded_input["method_call"]
    parameters = decoded_input["parameters"]

    method_args = method_call.split('(')[1].split(')')[0]
    method_args = method_args.split(", ")

    names = []

    for a in method_args:
        names.append(a.split(' ')[-1])

    values = [param['value'] for name in names for param in parameters if param['name'] == name]


    cmd = [method_call]

    for v in values:
        cmd.append(v)

    with open("script/upsert_commands.txt", 'a') as file:
        file.write(str(cmd) + "\n")





