from config import db
import sqlite3
from datetime import datetime

# returns list of all stock data from past n days orderd by a given param
def getRecentDOW(n, order):

    # retrieve all the data for stocks from most recent n dates
    data = db.execute("""SELECT * FROM DOW30 WHERE insert_date IN
                        (SELECT DISTINCT insert_date
                        FROM DOW30
                        ORDER BY insert_date
                        ASC LIMIT ?)
                        ORDER BY ? ASC""",
                        (n, order)).fetchall()
    return data


# returns list of all stock data from past n days orderd by a given param
def getRecentNASDAQ(n, order):

    # retrieve all the data for stocks from most recent n dates
    data = db.execute("""SELECT * FROM NASDAQ100 WHERE insert_date IN
                        (SELECT DISTINCT insert_date
                        FROM NASDAQ100
                        ORDER BY insert_date
                        ASC LIMIT ?)
                        ORDER BY (?) ASC""",
                        (n, order)).fetchall()
    return data


# returns all data of a stock in DOW30
def getDOWStock(ticker):

    return db.execute("SELECT * FROM DOW30 WHERE ticker = ?",
                        (ticker,)).fetchone()


# returns all data of a stock in NASDAQ100
def getNASDAQStock(ticker):

    return db.execute("SELECT * FROM NASDAQ100 WHERE ticker = ?",
                        (ticker,)).fetchone()

# given a list of results, prints data in readable format
# needs to know how many days of results is in the data
def prettyPrintResults(data):

    for entry in data:
        num_tweets = '(' + str(entry[3]) + ')'
        num_news = '(' + str(entry[4]) + ')'

        print(entry[0], ": news", round(entry[2],4), num_news, "twitter:",
        round(entry[1],4), num_tweets, "|", entry[5])
