#!/usr/bin/python3
"""Fetches custom status from a local test server using requests"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # <-- Test server URL
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
