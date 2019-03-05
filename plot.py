from database import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# given an array data for a single stock from database, create a line graph
def singleStockLineGraph(data):

    # put the info in each entry into respective array
    dates = []
    news_sent = []
    twitter_sent = []
    num_news = []
    num_tweets = []
    for entry in data:
        twitter_sent.append(entry[1])
        news_sent.append(entry[2])
        num_tweets.append(entry[3])
        num_news.append(entry[4])
        dates.append(entry[5])

    # create figure
    fig = plt.figure(figsize=(9,5))

    # create sentiment subplot
    plt.subplot(1, 2, 1)
    news_plot = plt.plot(dates, news_sent, 'r-')
    twitter_plot = plt.plot(dates, twitter_sent, 'b-')
    plt.ylabel('Sentiment Value')
    plt.xlabel("Date")
    plt.xticks(dates)
    plt.tight_layout()

    # create num results subplot
    plt.subplot(1, 2, 2)
    plt.plot(dates, num_news, 'r-')
    plt.plot(dates, num_tweets, 'b-')
    plt.ylabel('Number of Results')
    plt.xlabel('Date')
    plt.xticks(dates)
    plt.tight_layout()

    file_name = "test.png"

    plt.savefig(file_name)

    # return the file_name
    return file_name
