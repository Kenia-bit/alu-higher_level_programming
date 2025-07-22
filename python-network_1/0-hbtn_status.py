#!/usr/bin/python3
"""Fetches a URL and displays the body of the response with specific format"""

from urllib.request import urlopen
__import__('sys')

if __name__ == "__main__":
    sys = __import__('sys')
    url = sys.argv[1]
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
