#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using only requests"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException as e:
        print("Error:", e)
