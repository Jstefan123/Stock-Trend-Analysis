from config import db
import sqlite3
from datetime import datetime
import json

# given an index get the data from the most recent date
def getRecentData(index):

    data = db.execute("SELECT * FROM DOW30").fetchall()
