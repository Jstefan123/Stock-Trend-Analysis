import sqlite3
import os

# for news api
#news_api_key = "999e5995615f44ba8ed4cece981b1a09"
#news_api_key = "bfff1a9ffbdd4a49a737bee46084c0c3"
news_api_key = "89b8002c604141beb375abd022bb210d"
#news_api_key = "89de6b14f4164498b0161a78dcf88cd1"


# for twitter api
#twitter_api_key = "MmB5TCkf7PVCzxbgCCXh0C9I6"
#twitter_api_secret_key = "BqRHDkKJzJTTEzadfLtI3vQalyNc9gPjdMxOdM7pVLaMgq2pl4"
#twitter_token = "1101628164588167173-TZX6niJlRttzpQuMmXLDpcnDBJoFRY"
#twitter_secret_token = "6JiH6DP1nB2LmISJoiT4iC5yWwtoGpzf5sBgQzAtyR2fW"

twitter_api_key = "NJWHH6Zyv9ONco2KuYrmWHArm"
twitter_api_secret_key = "43GiTYAh61eTgatGk44hTi6fBV7Zw6v7E8AK65LwEYHmggO92w"
twitter_token = "1103049068052402177-nEkhHawLE76okjfEzlkDoLtiw9gdkF"
twitter_secret_token = "SizLLo62icfJU7eK7XDZrdjfUvPhio3jPPCT6Xhful1dB"

# IEX Cloud API
iex_token = "sk_52dd5c23ad974fcfbfd28966ee36ec60"

# create cursor to connect to database
db_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'StockTrender', 'data', 'database.sqlite3')
db = sqlite3.connect(db_file, isolation_level=None).cursor()

# list of DOW30 tickers for plotting X axis
dow30_tickers = ['AXP', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'DWDP', 'XOM', 'GS',
'HD', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE',
'PFE', 'PG', 'TRV', 'UNH', 'UTX', 'VZ', 'V', 'WBA', 'WMT', 'DIS']

nasdaq100_tickers = ['ATVI', 'ADBE', 'AMD', 'ALGN', 'ALXN', 'AMZN', 'AMGN',
'AAL', 'ADI', 'AAPL', 'AMAT', 'ASML', 'ADSK', 'ADP', 'AVGO', 'BIDU', 'BIIB',
'BMRN', 'CDNS', 'CELG', 'CERN', 'CHKP', 'CHTR', 'CTRP', 'CTAS', 'CSCO', 'CTXS',
'CMCSA', 'COST', 'CSX', 'CTSH', 'DLTR', 'EA', 'EBAY', 'EXPE', 'FAST', 'FB',
'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'HAS', 'HSIC', 'ILMN', 'INCY',
'INTC', 'INTU', 'ISRG', 'IDXX', 'JBHT', 'JD', 'KLAC', 'KHC', 'LRCX', 'LBTYA',
'LBTYK', 'LULU', 'MELI', 'MAR', 'MCHP', 'MDLZ', 'MNST', 'MSFT', 'MU', 'MXIM',
'MYL', 'NTAP', 'NFLX', 'NTES', 'NVDA', 'NXPI', 'ORLY', 'PAYX', 'PCAR', 'BKNG',
'PYPL', 'PEP', 'QCOM', 'REGN', 'ROST', 'SIRI', 'SWKS', 'SBUX', 'SYMC', 'SNPS',
'TTWO', 'TSLA', 'TXN', 'TMUS', 'ULTA', 'UAL', 'VRSN', 'VRSK', 'VRTX', 'WBA',
'WDC', 'WDAY', 'WLTW', 'WYNN', 'XEL', 'XLNX']
