#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status and display the body."""

from urllib import request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
