import config
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from textblob import TextBlob
import json


def getNewsRating(ticker, fullname):

    api = NewsApiClient(api_key=config.news_api_key)

    print("Processing", fullname, '(' + ticker + ')', "news articles")

    # only allow articles in the last 3 days
    oldest = datetime.date(datetime.now() - timedelta(hours=config.num_hours))

    # put the parameters together
    query = fullname + " OR $" + ticker

    data = api.get_everything(q=query, from_param=str(oldest), language='en',
                                  sort_by='popularity', page_size=100)

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
