#!/usr/bin/python3
"""This script takes in a URL, sends a request to it, and displays the value
of the X-Request-Id variable found in the header of the response"""

if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
