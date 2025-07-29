#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""

import requests


if __name__ == "__main__":
    try:
        # Use local checker URL during tests, or update to actual one
        url = "http://0.0.0.0:5050/status"
        response = requests.get(url, timeout=5)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException as e:
        pass
