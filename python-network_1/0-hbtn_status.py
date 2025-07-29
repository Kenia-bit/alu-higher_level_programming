#!/usr/bin/python3
"""A script that opens a TCP connection to a url and prints its content"""

from urllib.request import urlopen
if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf-8")))
