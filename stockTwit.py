import requests
import json
from datetime import datetime, timedelta

# returns the ID of a message closest to 830am
# uses AAPL discussion board because very popular
def getMaxID():

    # 830 am in UTC time
    time = datetime.now().replace(hour=13, minute=30, second=0, microsecond=0)

    url = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
    data = json.loads(requests.get(url).text)['messages']

    message_date = datetime.strptime(data[29]['created_at'], '%Y-%m-%dT%H:%M:%SZ')

    # keep requesting until a time past 830am is found
    while message_date >  time:
        # construct new url
        new_url = url + '?max=' + str(data[29]['id'])
        # request new data
        data = json.loads(requests.get(new_url).text)['messages']
        # format next oldest date
        message_date = datetime.strptime(data[29]['created_at'], '%Y-%m-%dT%H:%M:%SZ')

    #iterate through messages until first time past 830 is found
    # return first id before 830
    for message in data:
        message_date = datetime.strptime(message['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if message_date < time:
            return message['id']

# returns ID of a message closest to 5pm the day before
# uses AAPL discussion board because very popular
# starts at the max_id to save time/requests
def getMinID(max_id):

    # 5 pm previous day in UTC time
    time = datetime.now() - timedelta(days=1)
    time = time.replace(hour=22, minute=0, second=0, microsecond=0)

    url = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
    new_url = url + '?max=' + str(max_id)
    data = json.loads(requests.get(new_url).text)['messages']

    message_date = datetime.strptime(data[29]['created_at'], '%Y-%m-%dT%H:%M:%SZ')

    # keep requesting until a time past 830am is found
    while message_date >  time:
        # construct new url
        new_url = url + '?max=' + str(data[29]['id'])
        # request new data
        data = json.loads(requests.get(new_url).text)['messages']
        # format next oldest date
        message_date = datetime.strptime(data[29]['created_at'], '%Y-%m-%dT%H:%M:%SZ')

    #iterate through messages until first time before 530 pm is found
    for message in data:
        message_date = datetime.strptime(message['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if message_date < time:
            return message['id']


# calculates the average sentiment on stockTwit discussion board from approximately
# 1 hour after close to 1 hour before open before this trading session
# Bearish = -0.5, None = 0, Bullish = 0.5
def getStockTwitRating(ticker, min_id, max_id):

    #create the url
    url = 'https://api.stocktwits.com/api/2/streams/symbol/'
    url += (ticker + '.json')
    url += ('?max=' + str(max_id))
    url += ('&min=' + str(min_id))

    # retrieve first 30 messages that fit in this time period
    data = json.loads(requests.get(url).text)

    # make sure there are messages
    if data is not None:
        data = data['messages']
    else:
        return 0

    last_id = data[-1]['id']

    # retrive more until data min_id is reached
    while (last_id > min_id):
        url = 'https://api.stocktwits.com/api/2/streams/symbol/'
        url += (ticker + '.json')
        url += ('?max=' + str(last_id))
        url += ('&min=' + str(min_id))

        more_data = json.loads(requests.get(url).text)

        # make sure there are more messages
        if more_data is not None:
            more_data = more_data['messages']
        else:
            break
        data += more_data
        last_id = more_data[-1]['id']

    count = 0
    sentiment_sum = 0

    for message in data:
        if message["entities"]["sentiment"] == None:
            sentiment_sum += 0
        elif message["entities"]["sentiment"]["basic"] == 'Bullish':
            sentiment_sum += 1
        elif message["entities"]["sentiment"]["basic"] == 'Bearish':
            sentiment_sum -= 1
        count = count + 1

    if count == 0:
        return 0
    else:
        return sentiment_sum / count
