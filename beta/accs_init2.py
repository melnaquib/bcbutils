import requests
import json

from beta.rpc import _rpc
from beta.cfg import *

BCB = "0" * 27
beta = scfg["beta"]


def send(src, dst, amount):
    src = wallets[str(src)]
    dst = wallets[str(dst)]

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

def send_raw(src, dst, amount):
    src = wallets[str(src)]
    dst = wallets[str(dst)]

    amount = str(amount)
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

def recv(dst, hash):
    dst = wallets[str(dst)]

    args = {
        "action": "receive",
        "wallet": dst["wallet"],
        "account": dst["account"],
        "block": hash
    }
    rsp = _rpc(args)
    return rsp["block"]

def send_recv(src, dst, amount):
    hash = send(str(src), dst, amount)
    return hash, recv(str(dst), hash)

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

    i = 0
    total = 36 * 1000 * 1000 * 1000
    for i, name in enumerate(scfg["moves"]):
        acct_idx = beta + scfg["accs"]["moves"] + i
        amount = total * scfg["moves_funds"][name]
        send_recv(genesis_idx, acct_idx, amount)

    airdrop_idx = beta + scfg["accs"]["moves"] + scfg["accs"]["moves"].indexof("airdrop")
    repr_amount = scfg["repr"]["fund"]
    for i in scfg["default_repr"]:
        repr_idx = beta + i
        send_recv(airdrop_idx, repr_idx, repr_amount)
    for i in scfg["another_repr"]:
        repr_idx = beta + scfg["accs_repr"]["bgn"] + i
        send_recv(airdrop_idx, repr_idx, repr_amount)

    for i in scfg["default_repr"]:
        repr_idx = beta + i
        set_repr(repr_idx, repr_idx)
    for i in scfg["another_repr"]:
        repr_idx = beta + scfg["accs_repr"]["bgn"] + i
        set_repr(repr_idx, repr_idx)
        acct_idx = beta + i
        set_repr(acct_idx, repr_idx)


if __name__ == '__main__':
    main()