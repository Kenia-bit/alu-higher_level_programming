#!/usr/bin/python3
"""Fetches the status page and prints the response body."""

import requests
import sys

if __name__ == "__main__":
    # Default URL if none given
    url = "https://intranet.hbtn.io/status"
    if len(sys.argv) == 2:
        url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
