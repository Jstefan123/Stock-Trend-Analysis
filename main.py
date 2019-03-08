from database import *
from plot import *
from datetime import datetime, timedelta

def main():

    data = getRecentData('DOW30', 'stockTwit_sentiment', 'all')
    prettyPrintResults(data)



if __name__ == "__main__":
    main()
