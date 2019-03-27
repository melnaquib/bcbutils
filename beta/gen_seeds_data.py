import json

from rpc import _rpc, rpc


def main():

    seeds = open("data/seeds.txt")
    i = 0
    res = []
    for l in seeds:
        seed = l.strip()

        block = {
            "action": "deterministic_key",
            "seed": seed,
            "index": 0
        }

        rsp = _rpc(block)
        rsp["seed"] = seed
        res.append(rsp)

        i += 1

    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
