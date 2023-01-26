# Twitter-Fact-Bot

You will have to import time and use sleep function to post the tweet daily.
This script will run indefinitely, posting a new fact to Twitter every 24 hours. It uses the set data type to keep track of previously tweeted facts, which allows for fast lookups and prevents duplicates. If the fact has already been tweeted, the script will continue to get new fact until it gets the new one.

Please note that you will have to replace the placeholder text for the Twitter API credentials with your own. Additionally, you should handle the case where the API rate limits are hit and the script will have to wait before making the next request.

## Run 
In order to run the script I provided, you will need to have the following Python libraries installed:

* tweepy: A Python library for accessing the Twitter API
* randfacts: A Python library for generating random facts
* json: A Python library for handling JSON data

You can install these libraries using pip, the Python package installer, by running the following commands in your command line:
```
pip install tweepy
pip install randfacts
```
The json and time modules are built-in python modules and do not need installation.
Please make sure you have correct version of python installed in your system and python environment is setup properly.
You might also need to make sure that you have internet connection to run the script and use twitter API.

## Full Broke Down
The above code is a Python script that uses the Twitter API v2 and the randfacts library to post a daily fact to Twitter with the hashtag #fact. It also keeps track of previously tweeted facts to avoid duplicates. Here's a breakdown of what the code does:

Import the necessary libraries: tweepy, randfacts, json, time
Add your Twitter API credentials in the following variables: consumer_key, consumer_secret, access_token, access_token_secret. These credentials allow the script to authenticate with the Twitter API and access your Twitter account.

Authenticate with Twitter using the tweepy.OAuthHandler class and the API credentials.
Initialize an empty set tweeted_facts that will be used to keep track of previously tweeted facts
The script enters into infinite loop.

Within the loop, it gets a random fact from the randfacts library using the randfacts.get_fact() function.
Then it checks if the fact has already been tweeted using if fact not in tweeted_facts:

If the fact is new, it posts the fact to Twitter with the hashtag #fact using the api.update_status(fact + ' #fact') function.
The fact is added to the set tweeted_facts so that the script can keep track of it and avoid duplication in future.
If the fact is already tweeted, it continues to get new fact until it finds the new one.

The script waits for 24 hours before posting the next fact by using time.sleep(3600*24)
Please note that the script uses the set data type to keep track of previously tweeted facts. This allows for fast lookups and prevents duplicates. Additionally, the script sleeps for 24 hours before posting the next fact using time.sleep function which is imported from time library.
You may want to handle the rate limits and other errors that may occur while using the twitter API.

It is important to note that you will need to replace the placeholder text for the Twitter API credentials with your own, and you should handle the case where the API rate limits are hit and the script will have to wait before making the next request.
