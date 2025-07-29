#!/usr/bin/python3
"""Fetch status from local or remote URL with requests."""

import requests


def fetch_url(url):
    """Fetch URL content and print formatted response."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
        return True
    except requests.RequestException:
        return False


if __name__ == "__main__":
    local_url = "http://0.0.0.0:5050/status"
    remote_url = "https://intranet.hbtn.io/status"

    if not fetch_url(local_url):
        fetch_url(remote_url)
