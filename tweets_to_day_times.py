#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweet_reader import read_multiple_tweets_from_file
from sys import argv
from json import dumps, dump
import argparse


DAY = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
       14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}


def get_parser():
    """
    Get parser for command line arguments.
    """

    parser = argparse.ArgumentParser(description="tweets-to-dayjson")
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


def extract_time(timestamp):
    time = timestamp.split()[3]
    return time


def check_time_interval(time):
    hour, minute, second = time.split(":")
    DAY[int(hour)] += 1


def generate_json(output_to_save):
    f = open(output_to_save,"w")
    f.write(dumps(DAY))
    f.close()


def main():
    tweets = read_multiple_tweets_from_file(args.input)
    count = 0
    for i in tweets:
        timestamp = i['created_at']
        time = extract_time(timestamp=timestamp)
        check_time_interval(time=time)
    print count
    generate_json(output_to_save=args.output)
    print("JSON file created successfully.")


if __name__ == "__main__":
    parser = get_parser()
    if len(argv) == 1:
        print parser.parse_args(['-h'])
    args = parser.parse_args()
    main()

