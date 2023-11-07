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
    if after == "":
        count = [0] * len(word_list)

    request = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit),
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
