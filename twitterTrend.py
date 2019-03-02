import tweepy
import json
import re
from textblob import TextBlob
from datetime import datetime, timedelta

# api keys and tokens to set up with twitter developer account
api_key = "MmB5TCkf7PVCzxbgCCXh0C9I6"
api_secret_key = "BqRHDkKJzJTTEzadfLtI3vQalyNc9gPjdMxOdM7pVLaMgq2pl4"
token = "1101628164588167173-TZX6niJlRttzpQuMmXLDpcnDBJoFRY"
secret_token = "6JiH6DP1nB2LmISJoiT4iC5yWwtoGpzf5sBgQzAtyR2fW"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(token, secret_token)

# function to get data for a stock
# returns tweets as an array of JSON dicts
def getTwitterSentiment(ticker, full_name):

    print("Processing", full_name, '(' + ticker + ')', "tweets")

    # create the api entrypoint
    api = tweepy.API(auth)

    query = ticker + " AND " + full_name

    # only get tweets from the past 5 days
    oldest = datetime.date(datetime.now() - timedelta(days=5))

    # return the 100 most recent results (popular)
    results = api.search(q=query, count=100, since=oldest, tweet_mode="extended",
        result_type="mixed", include_entities=False)

    # Keep running total of sentiment values
    sentiment = 0
    count = 0

    # loop through resuls
    for tweet in results:

        # exract the full text of the tweet from the Status object
        text = json.loads(json.dumps(tweet._json))['full_text']

        # determine the sentiment value of the tweet
        analysis = TextBlob(text)
        value = analysis.sentiment.polarity
        sentiment += value
        count += 1

    # format data into a JSON dict
    obj = {}
    obj['ticker'] = ticker
    if count == 0:
        obj['twitter_sentiment'] = 0
        obj['num_tweets'] = 0
    else:
        obj['twitter_sentiment'] = sentiment / count
        obj['num_tweets'] = count

    return obj
