import json

import requests

btcb = "0" * 27

def rpc(data):
    url = "http://[::1]:15000"
    rsp = requests.post(url, json=data)
    res = json.loads(rsp.text)
    return res


def main():
    block = {
        "action": "deterministic_key",
        "seed": "",
        "index": "0"
    }

    seeds_file = open("data/seeds.txt")
    addresses_file = open("data/addresses.txt")
    for l in seeds_file:
        l = l.strip()
        block["seed"] = l
        res = rpc(block)
        print(res["account"])


if __name__ == '__main__':
    main()