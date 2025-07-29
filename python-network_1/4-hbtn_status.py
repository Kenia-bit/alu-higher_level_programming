#!/usr/bin/python3
"""Fetches a URL using requests and prints the response"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException as e:
        print("Error:", e)
