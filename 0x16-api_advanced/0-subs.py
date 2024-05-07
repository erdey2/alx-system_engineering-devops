#!/usr/bin/python3
"""extract data from api endpoints"""


def number_of_subscribers(subreddit):
    """ find the number of subscribers """
    import requests

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if data.status_code >= 300:
        return 0

    return data.json().get("data").get("subscribers")
