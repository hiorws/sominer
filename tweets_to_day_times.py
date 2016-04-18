#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweet_reader import read_multiple_tweets_from_file
from sys import argv
from json import dump, loads
import argparse
from datetime import datetime
from tqdm import tqdm


DAY = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
       14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}


def get_parser():
    """
    Get parser for command line arguments.
    """

    parser = argparse.ArgumentParser(description="tweets-to-day-times")
    parser.add_argument("-i",
                        "--input",
                        dest="input",
                        help="input file which contains json data about tweets",
                        default='-')
    parser.add_argument("-o",
                        "--output",
                        dest="output",
                        help="output file to save generated json")
    return parser


def time_from_time_stamp(timestamp):
    timestamp = int(timestamp) / 1000
    datetime_object = datetime.fromtimestamp(timestamp)
    return datetime_object


def extract_hour(timestamp):
    hour_interval = time_from_time_stamp(timestamp=timestamp).hour
    return hour_interval


def check_hour_interval(hour):
    DAY[int(hour % 24)] += 1


def generate_json(output_to_save):
    with open(output_to_save, 'w') as fp:
        dump(DAY, fp, indent=4, sort_keys=False)


def main():
    tweets = read_multiple_tweets_from_file(args.input)
    count = 0
    for tweet in tqdm(tweets):
        tweet = loads(tweet)
        timestamp = tweet['timestamp_ms']
        hour = extract_hour(timestamp=timestamp)
        check_hour_interval(hour=hour)
        count += 1
    print(str(count) + " tweets counted.")
    generate_json(output_to_save=args.output)
    print("JSON file created successfully.")


if __name__ == "__main__":
    parser = get_parser()
    if len(argv) == 1:
        print(parser.parse_args(['-h']))
    args = parser.parse_args()
    main()
