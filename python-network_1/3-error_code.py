#!/usr/bin/python3
"""A script that sends a request and handles HTTPError exception"""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with urlopen(url) as response:
                response_body = response.read().decode("utf-8")
                print(response_body)
        except HTTPError as error:
            print(f"Error code: {error.code}")
