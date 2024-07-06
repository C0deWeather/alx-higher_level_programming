#!/usr/bin/python3
"""THis script fetches a url"""

if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
