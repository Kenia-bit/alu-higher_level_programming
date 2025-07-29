#!/usr/bin/python3
"""Fetch status from local or remote URL using requests only."""

import requests


def fetch_status(url):
    """Fetch status from the given URL and print formatted response."""
    try:
        response = requests.get(url)
        text = response.text
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(text))
        return 0
    except requests.RequestException:
        return 1


if __name__ == "__main__":
    if fetch_status("http://0.0.0.0:5050/status") != 0:
        fetch_status("https://intranet.hbtn.io/status")
