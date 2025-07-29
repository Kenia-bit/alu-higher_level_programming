#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using requests"""

import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
