#!/usr/bin/python3
"""Fetch status from local or remote URL using requests."""

import requests


def fetch_status(url):
    """Fetch URL content and print formatted output."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
    except requests.RequestException:
        return False
    return True


if __name__ == "__main__":
    local_url = "http://0.0.0.0:5050/status"
    remote_url = "https://intranet.hbtn.io/status"

    if not fetch_status(local_url):
        fetch_status(remote_url)
