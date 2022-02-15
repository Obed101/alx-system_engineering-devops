#!/usr/bin/python3
""" This module uses flask to receive Reddit API """
import requests

def number_of_subscribers(subreddit):
    """ This methos counts the number of subscribers for one sub_r """
    url = 'https://www.reddit.com/dev/api/r/{}/about'.format(subreddit)
    n_of_subs = requests.get(url)

    return n_of_subs if n_of_subs else 0

