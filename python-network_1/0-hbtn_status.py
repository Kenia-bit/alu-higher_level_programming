#!/usr/bin/python3
"""Fetches a URL and prints the response body with formatting."""

from urllib import request

url = "http://0.0.0.0:5050/status"  # Change this line when testing on intranet

try:
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
except Exception as e:
    print("Error:", e)
