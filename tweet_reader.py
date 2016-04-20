#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps, loads, load
from sys import argv, exit


def read_multiple_tweets_from_file(file_path_to_read):
    """
    takes a file which contains multiple json and returns a list which contains python dicts which they have tweets
    :param file_path_to_read: file path
    :return: returns python list which includes dicts from readed tweets
    """

    tweet_list = []
    with open(file_path_to_read, 'r') as f:
        for line in f:
            if '{"limit":{"track":' not in line:
                tweet_dict = loads(line)
                tweet_list.append(tweet_dict)
    return tweet_list


def load_json_to_dict(json_file):
    """
    takes a json file and returns python dict
    :param json_file: gets json file path
    :return: returns python dict which includes whole info about tweet
    """

    with open(json_file) as data_file:
        data = load(data_file)
    return data


if __name__ == "__main__":
    if len(argv) == 1:
        print("Sample usage:")
        print("python " + str(argv[0]) + " sample.json")
        exit(0)
    file_name = argv[1]
    print(str(argv[1]) + " is reading...")
    tweets = read_multiple_tweets_from_file(file_name)
    print(tweets)
