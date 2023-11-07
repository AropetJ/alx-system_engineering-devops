#!/usr/bin/python3
"""Declares that queries an api"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    A function that queries a subreddit and
    returns th number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {
        "User-Agent": "ubuuntu:0x16.api.advanced:v1.0.0 (by /u/Aropet_Joel"
    }
    count = requests.get(url, headers=head, allow_redirects=False)
    if count.status_code == 404:
        return 0
    results = count.json().get("data")
    return results.get("subscribers")


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
