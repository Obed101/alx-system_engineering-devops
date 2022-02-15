#!/usr/bin/python3
""" This module uses flask to receive Reddit API """
import requests


def top_ten(subreddit):
    """ This method prints the top ten hot posts listed """

    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {"User-Agent": "Obed'sBrowser/5.0 (Windows NT 10.0)"}
    n_of_subs = requests.get(url, headers=headers, allow_redirects=False)

    if n_of_subs:
        for top in range(10):
            print(n_of_subs.json()['data'][top]['data']['title'])
    else:
        print('None')
