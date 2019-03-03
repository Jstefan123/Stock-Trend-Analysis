from data import getIndexData
from track import trackDowData, trackNASDAQData
import json

def main():

    data = getIndexData('DOW30')
    trackDowData(data)
    data = getIndexData('NASDAQ100')
    trackNASDAQData(data)


if __name__ == "__main__":
    main()
