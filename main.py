from update import insertData
from database import *

def main():

    #insertData('DOW30')
    #insertData('NASDAQ100')
    print(getRecentDOW())
    #print(getRecentNASDAQ())
    #print(getDOWStock('AAPL'))
    #print(getNASDAQStock('CSCO'))

if __name__ == "__main__":
    main()
