#!/usr/bin/python3
"""Declares that queries an api"""

import requests
import sys


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Qeries the Reddit API, parses the title of all hot articles, and
    prints a sorted count of given keywords

    Args:
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        subreddit (str): The subreddit to search.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    headers = {
        "User-Agent": "ubuntu:0x16.api.advanced:v1 (by /u/Aropet_Joel)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get("https://www.reddit.com/r/{}/hot/.json"
                            .format(subreddit), headers=headers,
                            params=params, allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for dic in results.get("children"):
        title = dic.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
