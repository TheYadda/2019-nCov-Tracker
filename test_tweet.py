#!/usr/bin/python3
# Test script for debugging cron, posts a test message with a timestamp

import time
import tweepy
import requests
import json

# Import our Twitter credentials from credentials.py
from credentials import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Get current UTC time
utctime = time.gmtime()

# Build tweet string
test_tweet = f""" AUTOMATED POST TEST
{utctime.tm_year:04}-{utctime.tm_mon:02}-{utctime.tm_mday:02} {utctime.tm_hour:02}:{utctime.tm_min:02}:{utctime.tm_sec:02} UTC"""

# Test print / terminal output
print(test_tweet)

# Send tweet
api.update_status(test_tweet)
