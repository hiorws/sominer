# sominer

----
#### sominer - mines so much things (under development)
sominer is a toolchain which helps to analyze and visualize tweets in real-time

---
#### Features

* Uses Twitter API to get tweets in real-time (uses [Tweepy](https://github.com/tweepy/tweepy "Tweepy Github"))
* Generate `json` files which can be used as an input in [Vega](https://github.com/vega/vega "Vega Github") to visualize
* Categorises tweets to the day times
* and more...

----

#### Installation

```
git clone https://github.com/hiorws/sominer.git
cd sominer
virtualenv -p python3 venv
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
python3 stream.py -q euthanasia -d data/
```

to prints tweets in json format

```
python3 tweet_reader.py stream_euthanasia.json

```

to split day times a tweet list

```
python3 tweets_to_day_times.py -i stream_euthanasia.json -o euthanasia_splitted.json
```

to create a JSON using data to use it with Vega

```
python3 vegalizer.py -t bar -d data/euthanasia_splitted.json -o data/bar_euthanasia.json

```

to use bar_euthanasia.json with Vega

```
vg2svg data/bar_euthanasia.json data/bar_euthanasia.svg

```

#### Help Screens
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

```
usage: tweets_to_day_times.py [-h] [-i INPUT] [-o OUTPUT]

tweets-to-day-times

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file which contains json data about tweets
  -o OUTPUT, --output OUTPUT
                        output file to save generated json
```


#### #TO-DO
- Integrate to a database
- Well documented




