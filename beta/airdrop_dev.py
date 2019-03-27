import requests
import json

from beta.rpc import _rpc
from beta.cfg import *

BCB = "0" * 27
beta = scfg["beta"]


def send(src, dst, amount):

    amount = int(amount)
    amount = str(amount) + BCB
    args = {
        "action": "send",
        "wallet": src["wallet"],
        "source": src["account"],
        "destination": dst["account"],
        "amount": amount,
        "id": dst["account"]
    }
    rsp = _rpc(args)
    return rsp["block"]


def main():

    airdrop_idx = beta + scfg["accs"]["moves"] + scfg["moves"].index("airdrop")
    airdrop = wallets[str(airdrop_idx)]

    # accs_file = open("data/addresses_000_099.txt")
    # accs_file = open("data/addresses_000_099.txt")

    airdrop_amount = scfg["airdrop_amount"]
    for i in range(scfg["airdrop_dev"]["bgn"], scfg["airdrop_dev"]["end"]):
        s = seeds[i]
        res = send(airdrop, s, airdrop_amount)

        if not i % 50:
            print(i, " ", res)


if __name__ == '__main__':
    main()