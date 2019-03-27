import requests
import json

from beta.rpc import _rpc

seeds = None
scfg = None
wallets = None
with open('data/seeds.json') as f:
    seeds = json.load(f)
with open('data/scfg.json') as f:
    scfg = json.load(f)
with open('data/wallets.json') as f:
    wallets = json.load(f)
