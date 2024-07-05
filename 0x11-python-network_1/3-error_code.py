#!/usr/bin/python3
"""This script sends a request to a url and displays
the body of the response"""

if __name__ == '__main__':
    import sys
    import urllib.request

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().encode('utf8')
            print(body)

    except urllib.error.HTTPError as e:
        print(e.code)
