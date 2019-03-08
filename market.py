import requests
from config import iex_token
import json


# returns the percent change for the previous trading session of a stock
def getPercentChange(ticker, fullname):


    print("Processing", fullname, '(' + ticker + ')', "market activity")

    # build request url
    url = 'https://cloud.iexapis.com/beta/stock/'
    url += ticker
    url += '/quote?filter=changePercent&token='
    url += iex_token

    data = json.loads(requests.get(url).text)

    return data['changePercent'] * 100
