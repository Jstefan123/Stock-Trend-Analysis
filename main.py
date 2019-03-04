from database import *

def main():

    data = getRecentNASDAQ(2, 'num_tweets')
    prettyPrintResults(data)

if __name__ == "__main__":
    main()
