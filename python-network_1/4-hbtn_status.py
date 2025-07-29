#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status using requests"""

import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # Use this instead of intranet URL
    try:
        response = requests.get(url, timeout=5)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.RequestException as e:
        print("Error:", e)
