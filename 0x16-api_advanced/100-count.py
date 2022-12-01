#!/usr/bin/python3
"""parses the title of all hot articles, and prints a sorted
count of given keywords"""
import requests
import re


def count_words(subreddit, word_list, hot_list=[], after=None):
    """parses the title of all hot articles"""
    URL = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    HEADERS = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return print_results(word_list, hot_list)

    response = requests.get(URL, headers=HEADERS, params=params)
    posts = response.json().get('data', {}).get('children', {})

