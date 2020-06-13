'''
In this, i will make a twitter bot who make a search operation on our given search string and
result an query out put.
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

search_string = 'Yeasin Arafath'
numberOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break