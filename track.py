import csv
import json
from datetime import datetime

# writes a line of sentiment values and a line representing number of number of
# results for each stock in index, each line starts with date
def trackDowData(json_obj):

    date = datetime.date(datetime.now())

    news_sentiments = [str(date)]
    num_news = [str(date)]
    twitter_sentiments = [str(date)]
    num_tweets = [str(date)]

    for stock in json_obj:
        news_sentiments.append(stock['news_sentiment'])
        num_news.append(stock['num_news'])
        twitter_sentiments.append(stock['twitter_sentiment'])
        num_tweets.append(stock['num_tweets'])

    # append to news data file
    with open('data/news/DOW_data.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(news_sentiments)
        writer.writerow(num_news)

    # append to twitter data file
    with open('data/twitter/DOW_data.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(twitter_sentiments)
        writer.writerow(num_tweets)

    return


# writes a line of sentiment values and a line representing number of number of
# results for each stock in index, each line starts with date
def trackNASDAQData(json_obj):

    date = datetime.date(datetime.now())

    news_sentiments = [str(date)]
    num_news = [str(date)]
    twitter_sentiments = [str(date)]
    num_tweets = [str(date)]

    for stock in json_obj:
        news_sentiments.append(stock['news_sentiment'])
        num_news.append(stock['num_news'])
        twitter_sentiments.append(stock['twitter_sentiment'])
        num_tweets.append(stock['num_tweets'])

    # append to news data file
    with open('data/news/NASDAQ_data.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(news_sentiments)
        writer.writerow(num_news)

    # append to twitter data file
    with open('data/twitter/NASDAQ_data.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(twitter_sentiments)
        writer.writerow(num_tweets)

    return
