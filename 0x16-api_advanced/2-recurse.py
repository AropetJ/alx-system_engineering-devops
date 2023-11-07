#!/usr/bin/python3
"""Declares that queries an api"""

from requests import get
import sys


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
    """
    global after
    after = None
    header = {'User-Agent': 'Aropet_Joel'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = get(url, params=parameters, headers=header,
                  allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)


if __name__ == "__main__":
    recurse(sys.argv[1])
