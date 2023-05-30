#!/usr/bin/python3

from tqdm import tqdm
import requests
import json
import csv

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def instruct_daemon(method, params):
    payload = json.dumps({"method": method, "params": params}, skipkeys=False)
    # print(payload)
    headers = {'content-type': "application/json"}
    try:
        response = requests.request("POST", "http://localhost:22023/json_rpc", data=payload, headers=headers)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
    except:
        print('No response from daemon, check daemon is running on this machine')

transaction_save_file = open('transaction-dump.json', 'r')
txn_hashes = json.load(transaction_save_file)

chunked_tx_hashes = chunks(txn_hashes, 1000)

special_txs = []
for chunk in tqdm(chunked_tx_hashes):
    result = instruct_daemon("get_transactions", {"txs_hashes": chunk, "decode_as_json": True, "tx_extra": True, "prune": True, "stake_info": True})["result"]["txs"]

    for tx in result:
        if "sn_state_change" in tx["extra"]:
            special_txs.append({"height": tx["block_height"], "tx_hash": tx["tx_hash"], "type": tx["extra"]["sn_state_change"]["type"]})
        if "sn_registration" in tx["extra"]:
            special_txs.append({"height": tx["block_height"], "tx_hash": tx["tx_hash"], "type": "registration"})

# extracting fieldnames
columns = ["height", "tx_hash", "type"]

# opening the file
with open("special_transactions.csv", "w", newline="") as f:
    # using dictwriter
    writer = csv.DictWriter(f, fieldnames=columns)
    # using writeheader function
    writer.writeheader()
    writer.writerows(special_txs)

# print(json.dumps(special_txs, indent=4, sort_keys=True))
