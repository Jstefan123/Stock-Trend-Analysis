from twitterTrend import getTwitterSentiment
from newsTrend import getNewsSentiment
import json

# function for sort that will sort the arry based on the value
# in the dict["sentiment"]
def sortFunc(dict):
    return dict['news_sentiment'] + dict['twitter_sentiment']

def main():

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open('DOW30.json', 'r') as infile:
        dow30 = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    results = getNewsSentiment('BWA', 'BorgWarner')

    twitter_results = getTwitterSentiment('BWA', 'BorgWarner')

    # analyze the news articles
    for stock in dow30:
        ticker = stock['ticker']
        full_name = stock['full_name']

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
