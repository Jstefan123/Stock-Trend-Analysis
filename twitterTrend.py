import tweepy
import json
from textblob import TextBlob

# api keys and tokens to set up with twitter developer account
api_key = "MmB5TCkf7PVCzxbgCCXh0C9I6"
api_secret_key = "BqRHDkKJzJTTEzadfLtI3vQalyNc9gPjdMxOdM7pVLaMgq2pl4"
token = "1101628164588167173-TZX6niJlRttzpQuMmXLDpcnDBJoFRY"
secret_token = "6JiH6DP1nB2LmISJoiT4iC5yWwtoGpzf5sBgQzAtyR2fW"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(token, secret_token)

# function to get data for a stock
# returns tweets as an array of JSON dicts
def getTwitterSentiment(ticker):

    # create the api entrypoint
    api = tweepy.API(auth)

    query = ticker

    # return the 100 most recent results (popular)
    results = api.search(q=query, count=100, tweet_mode="extended",
        result_type="popular", include_entities=False)

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

    #get the average sentiment
    sentiment_avg = sentiment / count
    return sentiment_avg
