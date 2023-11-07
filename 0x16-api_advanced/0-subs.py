#!/usr/bin/python3
"""Declares that queries an api"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Queries a subreddit and returns th number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = {
        "User-Agent": "ubuntu: 0x16.api.advanced: v1.0.0 (by /u/Aropet_Joel)"
        }
    response = requests.get(url, headers=agent, allow_redirects=False).json()
    try:
        return response.get('data').get('subscribers')
    except requests.exceptions.HTTPError as e:
        return 0
