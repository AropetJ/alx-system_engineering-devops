#!/usr/bin/python3
"""Declares that queries an api"""

from sys import argv
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries a subreddit and
    returns th number of subscribers
    """
    agent = {
        "User-Agent": "ubuntu: 0x16.api.advanced: v1.0.0 (by /u/Aropet_Joel)"
        }
    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit), headers=agent,
                            allow_redirects=False).json()

    try:
        return response.get('data').get('subscribers')
    except requests.exceptions.HTTPError as e:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
