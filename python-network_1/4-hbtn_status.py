#!/usr/bin/python3
"""Fetches the status from a URL using requests and displays the response body."""

import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    # url = "https://intranet.hbtn.io/status"

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
