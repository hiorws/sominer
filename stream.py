#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs

from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json
from get_config import get_config_keys
import sys


def get_parser():
    """Get parser for command line arguments."""

    parser = argparse.ArgumentParser(description="Sominer Twitter Streamer")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


class Listener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
        try:

            with codecs.open(self.outfile, 'a', encoding="utf-8") as f:
                json_writable = json.loads(data)
                f.write(json.dumps(json_writable))
                f.write("\n")
                return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'


@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


if __name__ == '__main__':
    parser = get_parser()
    if len(sys.argv) == 1:
        print(parser.parse_args(['-h']))
    args = parser.parse_args()
    api, auth = get_config_keys()

    twitter_stream = Stream(auth, Listener(args.data_dir, args.query))
    twitter_stream.filter(track=[args.query])
