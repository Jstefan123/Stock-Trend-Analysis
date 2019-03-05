import sqlite3
import os

# general
# number of days to look back for news/tweets
num_hours = 24

# for news api
news_api_key = "89b8002c604141beb375abd022bb210d"

# for twitter api
twitter_api_key = "NJWHH6Zyv9ONco2KuYrmWHArm"
twitter_api_secret_key = "43GiTYAh61eTgatGk44hTi6fBV7Zw6v7E8AK65LwEYHmggO92w"
twitter_token = "1103049068052402177-nEkhHawLE76okjfEzlkDoLtiw9gdkF"
twitter_secret_token = "SizLLo62icfJU7eK7XDZrdjfUvPhio3jPPCT6Xhful1dB"

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
