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
    query = fullname

    data = api.get_everything(q=query, from_param=str(oldest), language='en',
                                  sort_by='relevancy', page_size=100)

    # number of descriptions that are counted
    count = 0
    # running total of sentiment value
    sentiment = 0

    for article in data["articles"]:

        summary = article["description"]

        # if NoneType then skip
        if summary is None:
            continue

        # only if the ticker or name is mentioned in this string
        elif ticker in summary or fullname in summary:

            count += 1;
            # get the polarity rating from each summary
            analysis = TextBlob(summary)
            value = analysis.sentiment.polarity
            sentiment += value

    # format data into a JSON dict
        obj = {}
        obj['ticker'] = ticker
    if count == 0:
        obj['sentiment'] = 0
        obj['num_results'] = 0
    else:
        obj['sentiment'] = sentiment / count
        obj['num_results'] = count

    return obj
