from config import db
import sqlite3
from datetime import datetime
import json

# returns list of all stock data from most recent insert date in DOW30
def getRecentDOW():

    #get the most recent date
    most_recent_date = db.execute("""SELECT insert_date FROM DOW30
                            ORDER BY insert_date ASC LIMIT 1""").fetchone()[0]

    #retrieve all the data from this date
    return db.execute("SELECT * FROM DOW30 WHERE insert_date = ?",
                        (most_recent_date,)).fetchall()


# returns list of all stock data from most recent insert date in NASDAQ100
def getRecentNASDAQ():

    #get the most recent date
    most_recent_date = db.execute("""SELECT insert_date FROM NASDAQ100
                            ORDER BY insert_date ASC LIMIT 1""").fetchone()[0]

    #retrieve all the data from this date
    return db.execute("SELECT * FROM NASDAQ100 WHERE insert_date = ?",
                        (most_recent_date,)).fetchall()


# returns all data of a stock in DOW30
def getDOWStock(ticker):

    return db.execute("SELECT * FROM DOW30 WHERE ticker = ?",
                        (ticker,)).fetchone()


# returns all data of a stock in NASDAQ100
def getNASDAQStock(ticker):

    return db.execute("SELECT * FROM NASDAQ100 WHERE ticker = ?",
                        (ticker,)).fetchone()
