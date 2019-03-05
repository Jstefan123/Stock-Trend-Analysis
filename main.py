from database import *
from plot import *

def main():

    data = getRecentData('NASDAQ100', 'twitter_sentiment', 'all')
    
    print(data)

if __name__ == "__main__":
    main()
