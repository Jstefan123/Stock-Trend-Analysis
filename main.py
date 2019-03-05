from database import *

def main():

    data = getRecentData('NASDAQ100', 'news_sentiment', 'all')
    prettyPrintResults(data)

if __name__ == "__main__":
    main()
