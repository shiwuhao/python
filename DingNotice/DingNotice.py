# /usr/bin/env python3

import requests
import sys


def get(url, params):
    res = requests.get(url, params)
    result = res.text
    print(result)


def sendNotice(at, message):
    url = 'https://bi.juzifenqi.com/api/ding'
    params = {'at': at, 'message': message}
    print(params)
    get(url, params)


if __name__ == "__main__":
    argv = sys.argv
    message = argv[1]
    at = argv[2] if (len(argv) >= 3) else ''

    sendNotice(at, message)
