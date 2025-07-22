#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib with proper headers"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    req = Request(url, headers=headers)

    with urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
