from twitterTrend import getTwitterSentiment
from newsTrend import getNewsSentiment
import json

# function for sort that will sort the arry based on the value
# in the dict["sentiment"]
def sortFunc(dict):
    return dict['sentiment']

def main():

    # load in the list of DOW 30 stocks into a array of JSON dicts
    dict = {}
    with open('DOW30.json', 'r') as infile:
        dow30 = json.load(infile)['stocks']

    # list of stocks and thier sentiment values
    sentiments = []

    for stock in dow30:
        ticker = stock['ticker']
        full_name = stock['full_name']
        sentiments.append(getNewsSentiment(ticker, full_name))

    # sort the array from greatest to least
    sentiments.sort(reverse=True, key=sortFunc)

    # print results
    for elt in sentiments:
        print(elt)

if __name__ == "__main__":
    main()
