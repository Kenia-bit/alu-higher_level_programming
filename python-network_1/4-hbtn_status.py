#!/usr/bin/python3
"""Fetches status from a given URL using the requests module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alu-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except Exception as e:
        print("Error: {}".format(e))
