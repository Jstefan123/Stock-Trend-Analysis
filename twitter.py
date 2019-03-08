import config
import tweepy
import json
import re
from textblob import TextBlob
from datetime import datetime, timedelta

# removes all links and special characters from a tweet
def cleanTweet(tweet):

    tweet = tweet.split()

    # iterate and add to other array if not ticker or link
    clean_words = []

    for elt in tweet:
        if '$' not in elt and 'https' not in elt:
            clean_words.append(elt)

    return ' '.join(clean_words)

# function to get data for a stock
# returns tweets as an array of JSON dicts
def getTwitterRating(ticker, full_name):

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

    print(results)

    # Keep running total of sentiment values
    sentiment = 0
    count = 0

    # get rid of duplicate tweets
    unique_tweets = set()

    # loop through resuls
    for tweet in results:

        # clean the tweet of unneccesary tickers and links
        clean_tweet = cleanTweet(json.loads(json.dumps(tweet._json))['full_text'])
        # exract the full text of the tweet from the Status object
        unique_tweets.add(clean_tweet)

    # only consider unique tweets for sentiment analysis
    for tweet in unique_tweets:
        analysis = TextBlob(tweet)
        value = analysis.sentiment.polarity
        sentiment += value
        count += 1

    if count == 0:
        return  0
    else:
        return sentiment / count

# when the file is called, will update both tables and plots
if __name__ == "__main__":
    getTwitterRating('INTC', 'Intel')
