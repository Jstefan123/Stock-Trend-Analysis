import config
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from textblob import TextBlob
import json
import requests

def getNewsRating(ticker, fullname):

    api = NewsApiClient(api_key=config.news_api_key)

    # only allow articles from 1 hour after close in pervious day to
    # 1 hour before open this day (UTC TIME)
    yesterday = datetime.now() - timedelta(days=1)
    oldest = yesterday.replace(hour=22, minute=0, second=0, microsecond=0)
    newest = datetime.now().replace(hour=13, minute=30, second=0, microsecond=0)

    # put the parameters together
    query = fullname + " OR $" + ticker

    data = api.get_everything(q=query, from_param=str(oldest), to=str(newest),
                              language='en', sort_by='popularity', page_size=100)

    # only add unique articles
    unique_articles = set()
    for article in data["articles"]:
        unique_articles.add(article["title"])

    # number of descriptions that are counted
    count = 0
    # running total of sentiment value
    sentiment = 0

    for headline in unique_articles:

        # if NoneType then skip
        if headline is None:
            continue

        count += 1;
        # get the polarity rating from each summary
        analysis = TextBlob(headline)
        value = analysis.sentiment.polarity
        sentiment += value

    if count == 0:
        return 0
    else:
        return sentiment / count

if __name__ == "__main__":
    for stock in config.dow30_tickers:
        print(stock, getIEXNewsRating(stock))
