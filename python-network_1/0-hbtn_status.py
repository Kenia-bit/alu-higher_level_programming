#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and prints the response body"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://intranet.hbtn.io/status", headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
