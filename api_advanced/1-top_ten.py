#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        except (KeyError, IndexError):
            print("None")
    elif response.status_code == 404:
        print("None")
    elif response.status_code == 403:
        print("None")
    elif response.status_code == 302:
        # Reddit redirects for private/banned subreddits
        print("None")
    else:
        print("None")
