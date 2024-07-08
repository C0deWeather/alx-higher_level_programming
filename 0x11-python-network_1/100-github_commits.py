#!/usr/bin/python3
"""This script list 10 commits of a given repo using
the GiHub API"""

if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    query = {'per_page': 10}
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url, headers=headers, params=query)
    if response.status_code == 200:
        data = response.json()
        for commit in data:
            print(f"{commit.get('sha')}: \
{commit.get('commit').get('author').get('name')}")
