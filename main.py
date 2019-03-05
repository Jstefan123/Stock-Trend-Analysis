from database import *
from plot import createIndexPlots

def main():

    createIndexPlots('DOW30')
    createIndexPlots('NASDAQ100')

if __name__ == "__main__":
    main()
