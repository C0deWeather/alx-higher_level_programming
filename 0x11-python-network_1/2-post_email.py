#!/usr/bin/python3
"""This script takes in a URL and an email. sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response"""

if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
