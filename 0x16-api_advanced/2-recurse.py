#!/usr/bin/python3
"""Declares that queries an api"""

import requests
import sys


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function
    should return None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "ubuntu:0x16.api.advanced:v1 (by /u/Aropet_Joel)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for dic in results.get("children"):
        hot_list.append(dic.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list


if __name__ == "__main__":
    recurse(sys.argv[1])
