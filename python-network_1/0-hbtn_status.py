#!/usr/bin/python3
"""A script that opens a TCP connection to a URL and prints its content"""

from urllib.request import urlopen

if __name__ == "__main__":
    sys = __import__('sys')
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
