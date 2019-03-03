from config import db
import sqlite3
from datetime import datetime
import json

# returns list of all stock data from most recent insert date
def getRecentData(index):

    #get the most recent date
    most_recent_date = db.execute("""SELECT insert_date FROM DOW30
                            ORDER BY insert_date ASC LIMIT 1""").fetchone()[0]

    #retrieve all the data from this date
    data = db.execute("SELECT * FROM DOW30 WHERE insert_date = ?",
                        (most_recent_date,)).fetchall()

    return data
