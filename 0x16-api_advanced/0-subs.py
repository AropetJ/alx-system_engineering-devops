#!/usr/bin/python3
# get subs
import requests
import sys


def number_of_subscribers(subreddit):
    """subs"""
    head = {'User-Agent': 'Dan Kazam'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    i = requests.get(url, headers=head).json()
    try:
        return i.get('data').get('subscribers')
    except requests.exceptions.HTTPError as e:
        return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
