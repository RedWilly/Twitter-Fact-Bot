import tweepy
import randfacts
import json

# Add your Twitter API credentials here
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Keep track of previously tweeted facts
tweeted_facts = set()

while True:
    # Get a random fact from the randfacts library
    fact = randfacts.get_fact()

    # Check if the fact has already been tweeted
    if fact not in tweeted_facts:
        # Post the fact to Twitter with the hashtag #fact
        api.update_status(fact + ' #fact')
        tweeted_facts.add(fact)
    else:
        continue
    time.sleep(3600*24)
