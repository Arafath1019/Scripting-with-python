'''
In this, i will make a twitter bot who will find out a follower from my follow list
and follow back to my follower.
'''

import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # replace the consumer key and consumer secret as an string from the actual value from your twitter developer account app provide you.
auth.set_access_token(access_token, access_token_secret) # replace the access token and access token secret as an string from the actual value from your twitter developer account app provide you.

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(300)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Arafath':
        print(follower.name)
        follower.follow()
        break