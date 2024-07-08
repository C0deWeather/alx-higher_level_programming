#!/usr/bin/python3
"""This script takes the user's GitHub credentials and uses the GitHub
API to display your id"""

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {password}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = 'https://api.github.com/user'

    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        print(data.get('id'))
    else:
        pass
