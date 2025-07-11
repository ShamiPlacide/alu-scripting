#!/usr/bin/python3
"""
Function to query Reddit API for top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Query Reddit API and print the titles of the first 10 hot posts
    for a given subreddit
    
    Args:
        subreddit (str): The subreddit name to query
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'reddit-hot-posts-fetcher/1.0'
    }
    params = {
        'limit': 10
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if we got a valid response (200) and not a redirect
        if response.status_code == 200:
            data = response.json()
            
            # Check if the response contains valid subreddit data
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                
                # Print the titles of the first 10 hot posts
                for post in posts[:10]:
                    if 'data' in post and 'title' in post['data']:
                        print(post['data']['title'])
                return
        
        # If we get here, it's either a redirect, error, or invalid subreddit
        print("None")
        
    except (requests.RequestException, ValueError, KeyError):
        print("None")
