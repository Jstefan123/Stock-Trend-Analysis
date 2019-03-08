from config import db, nasdaq100_tickers, dow30_tickers
import sqlite3
from datetime import datetime

# returns <numStock> stocks in <index> from most recent day orderd by <orderBy>
def getRecentData(index, orderBy, numStocks):

    query = "SELECT * FROM " + index + """ WHERE insert_date IN
                        (SELECT insert_date
                        FROM """ + index + """ ORDER BY insert_date ASC
                        LIMIT 1)
                        ORDER BY """ + orderBy

    # if orderBy is ticker then order ASC, else order by DESC
    query += (orderBy == 'ticker') and ' ASC LIMIT ?' or ' DESC LIMIT ?'

    # if numStocks is 'all' then change to the size of nasdaq100/dow30
    if numStocks == 'all':
        numStocks = (index == 'DOW30') and len(dow30_tickers) or len(nasdaq100_tickers)

    return db.execute(query, (numStocks,)).fetchall()


# returns all data of a stock in DOW30
def getDOWStock(ticker):

    return db.execute("SELECT * FROM DOW30 WHERE ticker = ?",
                        (ticker,)).fetchall()


# returns all data of a stock in NASDAQ100
def getNASDAQStock(ticker):

    return db.execute("SELECT * FROM NASDAQ100 WHERE ticker = ?",
                        (ticker,)).fetchall()

# given a list of results, prints data in readable format
# needs to know how many days of results is in the data
def prettyPrintResults(data):

    for entry in data:
        print(entry[0], ": news", round(entry[2],4), "twitter:",
        round(entry[1],4), "percent_change: ", round(entry[3],4), "|", entry[4])
