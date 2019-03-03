from twitterTrend import getTwitterSentiment
from newsTrend import getNewsSentiment
import json


def getIndexData(index):

    # determine which index to use
    if index == 'DOW30':
        json_file = 'DOW30.json'
    else:
        json_file = 'NASDAQ100.json'

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open(json_file, 'r') as infile:
        index = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    # analyze the news articles
    for stock in index:
        ticker = stock['ticker']
        full_name = stock['full_name']

        results = getNewsSentiment(ticker, full_name)
        twitter_results = getTwitterSentiment(ticker, full_name)

        # add the num and sentiment elements into results
        results['twitter_sentiment'] = twitter_results['twitter_sentiment']
        results['num_tweets'] = twitter_results['num_tweets']

        sentiments.append(results)

    return sentiments
