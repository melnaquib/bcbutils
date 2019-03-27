import json

import requests


def rpc(args):
    host = "[::1]"
    # host = "localhost"
    port = "15000"
    url = "http://" + host + ":" + port
    try:
        res = requests.post(url=url, json=args)
        return json.loads(res.text)
    except Exception as ex:
        print(ex)

    return {
        "error": True
    }

def _rpc(args):
    host = "[::1]"
    port = "15000"
    url = "http://" + host + ":" + port
    res = requests.post(url=url, json=args)
    return json.loads(res.text)
