#!/usr/bin/python3
"""Fetches status from a given URL using the requests module"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # Change to https://alu-intranet.hbtn.io/status when testing remotely

    try:
        response = requests.get(url)
        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except Exception as e:
        print("Error: {}".format(e))
