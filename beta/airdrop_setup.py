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
    if "error" in rsp:
        # return open_(dst, hash)
        return rsp["error"]
    return rsp["block"]

def open_(dst, hash):

    args = {
        "action": "block_create",
        "type": "open",
        "wallet": dst["wallet"],
        "account": dst["account"],
        "representative": dst["account"],
        "source": hash
    }
    rsp = _rpc(args)

    args = {
        "action": "process",
        "block": rsp["block"]
    }
    rsp = _rpc(args)
    return rsp["hash"]

def send_recv(src, dst, amount):
    hash = send(str(src), dst, amount)
    return hash, recv(str(dst), hash)

def set_repr(acct, repr):
    acct = wallets[str(acct)]
    repr = wallets[str(repr)]

    args = {
        "action": "account_representative_set",
        "wallet": acct["wallet"],
        "account": acct["account"],
        "representative": repr["account"]
    }
    rsp = _rpc(args)
    return rsp["block"]


def main():

    airdrop_idx = beta + scfg["accs"]["moves"] + scfg["moves"].index("airdrop")

    # accs_file = open("data/addresses_000_099.txt")
    # accs_file = open("data/addresses_000_099.txt")

    for l in open():
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

    burn_proxy_repr_idx = burn_proxy_idx + scfg["accs_repr"]["bgn"]
    set_repr(burn_proxy_idx, burn_proxy_repr_idx)


if __name__ == '__main__':
    main()