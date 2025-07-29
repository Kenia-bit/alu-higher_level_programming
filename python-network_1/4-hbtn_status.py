#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException:
        pass
