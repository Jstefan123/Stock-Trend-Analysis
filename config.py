import sqlite3
import os

# general
# number of days to look back for news/tweets
num_hours = 24

# for news api
news_api_key = "89b8002c604141beb375abd022bb210d"

# for twitter api
twitter_api_key = "MmB5TCkf7PVCzxbgCCXh0C9I6"
twitter_api_secret_key = "BqRHDkKJzJTTEzadfLtI3vQalyNc9gPjdMxOdM7pVLaMgq2pl4"
twitter_token = "1101628164588167173-TZX6niJlRttzpQuMmXLDpcnDBJoFRY"
twitter_secret_token = "6JiH6DP1nB2LmISJoiT4iC5yWwtoGpzf5sBgQzAtyR2fW"

# create cursor to connect to database
db_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'StockTrender', 'data', 'database.sqlite3')
db = sqlite3.connect(db_file, isolation_level=None).cursor()
