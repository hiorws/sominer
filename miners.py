#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import json


def process_or_store(tweet):
    print(json.dumps(tweet))


def print_time_line(api, number):
    for status in tweepy.Cursor(api.home_timeline).items(number):
        process_or_store(status._json)


def print_friends(api):
    for friend in tweepy.Cursor(api.friends).items():
        process_or_store(friend._json)


def print_my_tweets(api):
    for tweet in tweepy.Cursor(api.user_timeline).items():
        process_or_store(tweet._json)
