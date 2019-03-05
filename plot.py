from database import *
from config import dow30_tickers, nasdaq100_tickers
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

    # close any figure that may be open
    plt.close()

    # create figure
    fig = plt.figure(figsize=(9,5))

    # create sentiment subplot
    plt.subplot(1, 2, 1)
    plt.plot(dates, news_sent, 'r-', label="News")
    plt.plot(dates, twitter_sent, 'b-', label="Twitter")
    plt.ylabel('Sentiment Value')
    plt.xlabel("Date")
    plt.xticks(dates)
    plt.legend()
    plt.tight_layout()

    # create num results subplot
    plt.subplot(1, 2, 2)
    plt.plot(dates, num_news, 'r-', label="News")
    plt.plot(dates, num_tweets, 'b-', label="Twitter")
    plt.ylabel('Number of Results')
    plt.xlabel('Date')
    plt.xticks(dates)
    plt.legend()
    plt.tight_layout()

    # return the plot
    return plt

# given an index, creates the plots for all the stocks in that data
# and saves/rewrites in /plots/<index>/<ticker>.png
def updateIndexPlots(index):

    # get the index stock list
    stock_list = (index == 'DOW30') and dow30_tickers or nasdaq100_tickers

    # iterate through each stock ticker
    for ticker in stock_list:

        print("Creating", ticker, "plot")

        # get respective stock's data
        data = (index == 'DOW30') and getDOWStock(ticker) or getNASDAQStock(ticker)

        #create the figure
        figure = singleStockLineGraph(data)

        # create the file path to save to
        save_path = 'plots/' + index + '/' + ticker
        plt.savefig(save_path)
