#!/usr/bin/python3
"""A script that makes a request and checks the status code."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with requests.get(url) as response:
            if response.status_code < 400:
                print(response.text)
            else:
                print(f"Error code: {response.status_code}")
