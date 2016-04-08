#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import config
from tweepy import OAuthHandler


def get_tokens_from_config():
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_secret = config.access_secret
    return consumer_key, consumer_secret, access_token, access_secret


def get_config():
    consumer_key, consumer_secret, access_token, access_secret = get_tokens_from_config()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api, auth
