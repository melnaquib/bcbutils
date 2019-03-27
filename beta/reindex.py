import requests
import json

from beta.rpc import _rpc

# seeds = None
# with open('data/wallets.json') as f:
#     seeds = json.load(f)

seeds = None
with open('data/seeds.json') as f:
    seeds = json.load(f)


def main():
    res = []
    for i in range(len(seeds)):
        seeds[i]["idx"] = i
        res.append(seeds[i])

    print(json.dumps(res, indent=2))

if __name__ == '__main__':
    main()
