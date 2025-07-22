#!/usr/bin/python3
"""A script that makes a POST request and handles JSON object"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    try:
        with requests.post(url, data=data) as response:
            json_object = response.json()
            if len(json_object) == 0:
                print("No result")
            else:
                print(f"[{json_object['id']}] {json_object['name']}")
    except Exception as error:
        print("Not a valid JSON")
