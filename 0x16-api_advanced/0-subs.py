#!/usr/bin/python3
""" This module uses flask to receive Reddit API """
import requests

def number_of_subscribers(subreddit):
    """ This methos counts the number of subscribers for one sub_r """
    url = 'https://www.reddit.com/dev/api/r/{}/about'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0"}
    n_of_subs = requests.get(url, headers=headers, allow_redirects=False)
    print(n_of_subs.status_code)
    return n_of_subs if n_of_subs and not n_of_subs.staus_code == 404 else 0

