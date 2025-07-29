#!/usr/bin/python3
"""Fetches status content from a given URL using the requests module."""

import requests


def fetch_status(url):
    """Fetch and print response from the given URL."""
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_status("http://0.0.0.0:5050/status")
    # If your checker wants the intranet URL, uncomment the next line and comment out the one above:
    # fetch_status("https://intranet.hbtn.io/status")
