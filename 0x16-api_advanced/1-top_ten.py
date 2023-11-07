#!/usr/bin/python3
"""Declares that queries an api"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "ubuntu:0x16.api.advanced:v1 (by /u/Aropet_Joel)"
    }
    parameters = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(dic.get("data").get("title")) for dic in results.get("children")]


if __name__ == "__main__":
    top_ten(sys.argv[1])
