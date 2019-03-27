import requests
import json

from beta.rpc import _rpc
from beta.cfg import *

BCB = "0" * 27
beta = scfg["beta"]


def send(src, dst, amount):

    try:
        amount = int(amount)
        amount = str(amount) + BCB
        args = {
            "action": "send",
            "wallet": src["wallet"],
            "source": src["account"],
            "destination": dst,
            "amount": amount,
            "id": dst
        }
        rsp = _rpc(args)
        return rsp["block"]
    except Exception as ex:
        print(dst)
    return dst


def main():

    airdrop_idx = beta + scfg["accs"]["moves"] + scfg["moves"].index("airdrop")
    airdrop = wallets[str(airdrop_idx)]

    accs_file = open("data/accs1.txt")

    airdrop_amount = scfg["airdrop_amount"]
    i = 0
    for l in accs_file:
        dst = l.strip()
        res = send(airdrop, dst, airdrop_amount)

        if not i % 50:
            print(i, " ", res)
        i = i + 1


if __name__ == '__main__':
    main()