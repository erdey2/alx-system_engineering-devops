#!/usr/bin/python3
"""extract data from api endpoints"""
import requests


def number_of_subscribers(subreddit):
    """ find the number of subscribers """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    try:
        top_ten = response.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")
