#!/usr/bin/python3
"""Fetches the status from a given URL and prints the response content."""

import requests


def fetch_status(url):
    """Fetch and display the response body from a given URL."""
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")


if __name__ == "__main__":
    fetch_status("http://0.0.0.0:5050/status")
    # To test intranet, use this instead:
    # fetch_status("https://intranet.hbtn.io/status")
