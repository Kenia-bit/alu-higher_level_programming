#!/usr/bin/python3
"""A script that usese the request library to make a request"""

import requests
if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
