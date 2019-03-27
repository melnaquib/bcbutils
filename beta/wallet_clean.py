import requests
import json

from beta.rpc import _rpc
from beta.cfg import *

BCB = "0" * 27
beta = scfg["beta"]


def clean(wid):
    args = {
        "action": "wallet_destroy",
        "wallet": wid
    }
    rsp = _rpc(args)
    return rsp["destroyed"]


def main():

    for i, w in wallets.items():
        res = clean(w["wallet"])
        print(res)

if __name__ == '__main__':
    main()