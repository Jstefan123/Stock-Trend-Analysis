from newsapi import NewsApiClient
from datetime import datetime, timedelta
from textblob import TextBlob
import json


base_url = "https://newsapi.org/v2/everything"
api_key = "999e5995615f44ba8ed4cece981b1a09"
api = NewsApiClient(api_key=api_key)

def getNewsSentiment(ticker, fullname):

    print("Processing", fullname, '(' + ticker + ')', "news articles")

    # only allow articles in the last 3 days
    oldest = datetime.date(datetime.now() - timedelta(days=5))

    # put the parameters together
    query = fullname + " AND " + ticker

    data = api.get_everything(q=query, from_param=str(oldest), language='en',
                                  sort_by='popularity', page_size=100)

    # number of descriptions that are counted
    count = 0
    # running total of sentiment value
    sentiment = 0

    for article in data["articles"]:

        summary = article["description"]

        # if NoneType then skip
        if summary is None:
            continue

        count += 1;
        # get the polarity rating from each summary
        analysis = TextBlob(summary)
        value = analysis.sentiment.polarity
        sentiment += value

    # format data into a JSON dict
        obj = {}
        obj['ticker'] = ticker
    if count == 0:
        obj['news_sentiment'] = 0
        obj['num_news'] = 0
    else:
        obj['news_sentiment'] = sentiment / count
        obj['num_news'] = count

    return obj
