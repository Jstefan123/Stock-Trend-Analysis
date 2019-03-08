from config import db
from plot import updateIndexPlots
from twitter import getTwitterRating
from news import getNewsRating
from market import getPercentChange
from datetime import datetime, timedelta
import json
import sqlite3

# inserts data for this index into database
def insertData(index):

    date = datetime.date(datetime.now())

    if index == 'DOW30':
        data = getIndexData('DOW30.json')
        for stock in data:
            db.execute("INSERT INTO DOW30 VALUES (?,?,?,?,?)",
            (stock['ticker'], stock['twitter_sentiment'], stock['news_sentiment'],
            stock['percent_change'], date))
    else:
        data = getIndexData('NASDAQ100.json')
        for stock in data:
            db.execute("INSERT INTO NASDAQ100 VALUES (?,?,?,?,?)",
            (stock['ticker'], stock['twitter_sentiment'], stock['news_sentiment'],
            stock['percent_change'], date))

    return

def getIndexData(json_file):

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open('data/' + json_file, 'r') as infile:
        index = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    # analyze the news articles
    for stock in index:
        ticker = stock['ticker']
        full_name = stock['full_name']

        news_results = getNewsRating(ticker, full_name)
        twitter_results = getTwitterRating(ticker, full_name)
        percent_change = getPercentChange(ticker, full_name)

        # create a dict of the results
        results = {}
        results['ticker'] = ticker
        results['news_sentiment'] = news_results
        results['twitter_sentiment'] = twitter_results
        results['percent_change'] = percent_change

        sentiments.append(results)

    return sentiments

# when the file is called, will update both tables and plots
if __name__ == "__main__":
    insertData('DOW30')
    #insertData('NASDAQ100')
    updateIndexPlots('DOW30')
    #updateIndexPlots('NASDAQ100')
