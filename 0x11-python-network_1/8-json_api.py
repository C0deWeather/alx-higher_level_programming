#!/usr/bin/python3
"""This script takes in a letter and sends a post request to a given
url with the letter as a parameter"""

if __name__ == '__main__':
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
