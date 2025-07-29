#!/usr/bin/python3
"""Fetches the status from a URL and displays the body content."""

import requests


def fetch_status(url):
    """Fetches the status text from the given URL."""
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # You can change the URL here if needed
    url = "http://0.0.0.0:5050/status"
    # url = "https://intranet.hbtn.io/status"

    content = fetch_status(url)
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
