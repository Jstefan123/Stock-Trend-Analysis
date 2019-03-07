from database import *
from plot import *

def main():

    data = getRecentData('NASDAQ100', 'num_news', 'all')
    prettyPrintResults(data)

if __name__ == "__main__":
    main()
