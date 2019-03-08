from database import *
from plot import *

def main():

    data = getRecentData('DOW30', 'news_sentiment', 'all')
    prettyPrintResults(data)

if __name__ == "__main__":
    main()
