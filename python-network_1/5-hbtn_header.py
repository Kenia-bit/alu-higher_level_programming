#!/usr/bin/python3
"""A script that makes a request and retrieves a header."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with requests.get(url) as response:
            headers = response.headers
            id_header = headers.get("X-Request-Id")
            print(id_header)
