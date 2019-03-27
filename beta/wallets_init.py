import requests
import json

from beta.cfg import *
from beta.rpc import _rpc

beta = scfg["beta"]

def wallet_create(seed):
  seed["repr"] = seed["account"]
  seed["repr_idx"] = seed["idx"]
  args = {"action": "wallet_create"}
  rsp = _rpc(args)
  seed["wallet"] = rsp["wallet"]

  args = {
        "action": "wallet_change_seed",
        "wallet": seed["wallet"],
        "seed": seed["seed"],
        "count": 2
  }
  rsp = _rpc(args)
  return seed

def main():
    res = {}
    for i in range(beta, beta + 50):
        seeds[i]["repr_idx"] = i
        s = wallet_create(seeds[i])
        res[i] = s

    another_repr = [1, 9, 11, 12,13,14, 15, 16, 17, 18, 19]
    for i in another_repr:
        repr_idx = res[beta + i]["repr_idx"] + scfg["accs_repr"]["bgn"]
        res[beta + i]["repr_idx"] = repr_idx
        res[beta + i]["repr"] = seeds[repr_idx]["account"]

    print(json.dumps(res, indent=2))

if __name__ == '__main__':
    main()
