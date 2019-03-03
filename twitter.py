import config
import tweepy
import json
from textblob import TextBlob
from datetime import datetime, timedelta

# function to get data for a stock
# returns tweets as an array of JSON dicts
def getTwitterSentiment(ticker, full_name):

    auth = tweepy.OAuthHandler(config.twitter_api_key, config.twitter_api_secret_key)
    auth.set_access_token(config.twitter_token, config.twitter_secret_token)

    print("Processing", full_name, '(' + ticker + ')', "tweets")

    # create the api entrypoint
    api = tweepy.API(auth)

    query = ticker + " AND " + full_name

    # only get tweets from the past 5 days
    oldest = datetime.date(datetime.now() - timedelta(hours=config.num_hours))

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
