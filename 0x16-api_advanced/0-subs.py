#!/usr/bin/python3
"""extract data from api endpoints"""
import requests


def number_of_subscribers(subreddit):
    """ find the number of subscribers """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    count = response.json().get('data').get('subscribers')
    return count
