#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # or https://intranet.hbtn.io/status
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    except Exception as e:
        print("Error:", e)
