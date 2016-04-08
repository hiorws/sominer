# sominer

----
#### sominer  - mine so much things (under development)
sominer is a python tool for analyze and visualize tweets that uses tweepy

---
#### Features

----

#### Installation

```
git clone https://github.com/hiorws/sominer.git
cd sominer
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cp config.py.sample config.py
mkdir data
```
and edit the `config.py` add your tokens

----
#### Sample Usage

to get public tweets includes about euthanasia

```
python stream -q euthanasia -d data
```

to prints tweets in json format

```
python tweet_printer.py
Enter .json file name to read and print:stream_euthanasia.json
```


#### Help Screen
```
usage: stream.py [-h] [-q QUERY] [-d DATA_DIR]

Sominer Twitter Streamer

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Query/Filter
  -d DATA_DIR, --data-dir DATA_DIR
                        Output/Data Directory
```

#### TO-DO
- Integrate with a visualization tool
- Integrate to a database
- Well documented




