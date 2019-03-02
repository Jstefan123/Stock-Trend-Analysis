from twitterTrend import getTwitterSentiment
from newsTrend import getNewsSentiment
import json

# function for sort that will sort the arry based on the value
# in the dict["sentiment"]
def sortFunc(dict):
    sum = dict['news_sentiment'] + dict['twitter_sentiment']
    count = dict['num_news'] + dict['num_tweets']
    if count == 0:
        return 0
    else:
        return sum / count

def main():

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open('DOW30.json', 'r') as infile:
        dow30 = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    # analyze the news articles
    for stock in dow30:
        ticker = stock['ticker']
        full_name = stock['full_name']

        results = getNewsSentiment(ticker, full_name)

        twitter_results = getTwitterSentiment(ticker, full_name)

        # add the num and sentiment elements into results
        results['twitter_sentiment'] = twitter_results['twitter_sentiment']
        results['num_tweets'] = twitter_results['num_tweets']

        sentiments.append(results)


    # sort the array from greatest to least
    sentiments.sort(reverse=True, key=sortFunc)

    # print results
    for elt in sentiments:
        print(elt)

if __name__ == "__main__":
    main()
