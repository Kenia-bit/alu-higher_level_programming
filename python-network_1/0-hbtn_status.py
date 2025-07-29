#!/usr/bin/python3
"""Fetches a URL and prints formatted response"""

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("http://0.0.0.0:5050/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
