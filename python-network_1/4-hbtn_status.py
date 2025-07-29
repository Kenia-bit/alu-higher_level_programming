#!/usr/bin/python3
"""
Fetch status from URL, prefer local if available.
Uses requests only.
"""

import requests
import sys


def fetch_status(url):
    """Fetches URL and prints body response info."""
    try:
        r = requests.get(url)
        print("Body response:")
        print(f"\t- type: {type(r.text)}")
        print(f"\t- content: {r.text}")
        return True
    except requests.RequestException:
        return False


if __name__ == "__main__":
    # Try local first
    local_url = "http://0.0.0.0:5050/status"
    remote_url = "https://intranet.hbtn.io/status"

    if not fetch_status(local_url):
        fetch_status(remote_url)
