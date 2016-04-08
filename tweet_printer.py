import json


def print_tweets_from_file(file_name):
    with open('data/' + str(file_name) + '.json', 'r') as f:
        line = f.readline()
        tweet = json.loads(line)
        print(json.dumps(tweet, indent=4))


if __name__ == "__main__":
    file_to_read_and_print = raw_input("Enter .json file name to read and print:")
    print_tweets_from_file(file_name=file_to_read_and_print)
