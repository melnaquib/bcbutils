import requests
import json

from beta.rpc import _rpc
from beta import wallets_init

BCB = "0" * 27

seeds = None
scfg = None
wallets = None
with open('data/seeds.json') as f:
    seeds = json.load(f)
with open('data/scfg.json') as f:
    scfg = json.load(f)
with open('data/wallets.json') as f:
    wallets = json.load(f)

def send(src, dst, amount):
    src = wallets[src]
    dst = wallets[dst]

    args = {
        "action": "send",
        "wallet": src["wallet"],
        "source": src["account"],
        "destination": dst["account"],
        "amount": amount + BCB,
        "id": dst["account"]
    }
    rsp = _rpc(args)
    return rsp["block"]

def recv(dst, hash):
    dst = wallets[dst]

    args = {
        "action": "receive",
        "wallet": dst["wallet"],
        "account": dst["account"],
        "block": hash
    }
    rsp = _rpc(args)
    return rsp["block"]

def send_recv(src, dst, amount):
    hash = send(src, dst, amount)
    return hash, recv(dst, amount)

def set_repr(acct, repr):
    acct = wallets[acct]
    repr = wallets[repr]

    args = {
        "action": "account_representative_set",
        "wallet": acct["wallet"],
        "account": acct["account"],
        "representative": repr["account"]
    }
    rsp = _rpc(args)
    return rsp["block"]

def main():
    genesis_idx = scfg["beta"] + scfg["accs"]["genesis"]
    genesis = wallets[genesis_idx]

    i = 0
    total = 36 * 1000 * 1000 * 1000
    for k, v in scfg["funds"]:
        acct_idx = scfg["beta"] + scfg["accs"]["move_idx"] + i
        repr_idx = scfg["beta"] + scfg["accs"]["move_reprs_idx"] + i

        send_recv(genesis_idx, repr_idx, scfg["funds_reprs_amount"])
        set_repr(repr_idx, repr_idx)

        fund = int(total * v)
        send_recv(genesis_idx, acct_idx, fund)
        set_repr(acct_idx, repr_idx)


if __name__ == '__main__':
    main()