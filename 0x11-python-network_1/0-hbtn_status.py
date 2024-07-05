#!/usr/bin/python3
"""This module sends a request using the urllib module and prints the response
in a given format"""

import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf8'))
