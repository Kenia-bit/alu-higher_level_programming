#!/usr/bin/python3
"""Fetches a URL and prints formatted response"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alu-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
