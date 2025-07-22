#!/usr/bin/python3
"""A script that makes a post request with requests library"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        with requests.post(url, data={"email": email}) as response:
            print(response.text)
