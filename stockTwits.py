import requests
import json
from datetime import datetime, timedelta
from twitter import cleanText
from config import dow30_tickers

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

    # retrieve up to 30 messages that fit in time period
    data = json.loads(requests.get(url).text)

    # make sure there are messages
    if not data is None:
        data = data['messages']
    else:
        return 0

    count = 0
    sentiment_sum = 0

    for message in data:
        if message["entities"]["sentiment"] == None:
            sentiment_sum += 0
        elif message["entities"]["sentiment"]["basic"] == 'Bullish':
            sentiment_sum += 0.5
        elif message["entities"]["sentiment"]["basic"] == 'Bearish':
            sentiment_sum -= 0.5
        count = count + 1

    if count == 0:
        return 0
    else:
        return sentiment_sum / count

def updateTrainingData(ticker):

    print('Processing', ticker, 'data')
    
    url = 'https://api.stocktwits.com/api/2/streams/symbol/' + ticker + '.json'
    data = json.loads(requests.get(url).text)['messages']

    dataset = {}

    # open existing training data file
    with open('data/training_data.json') as infile:
        dataset = json.load(infile)

    # request 5 times
    for i in range(0,5):

        # add all 30 message bodies and their sentiments
        for message in data:

            context = {}
            # remove tickers, handles, links from text
            body = cleanText(message['body'])

            # do not add blank texts
            if not body is None:

                context['text']  = body
                # add the sentiment
                if message["entities"]["sentiment"] == None:
                    continue
                elif message["entities"]["sentiment"]["basic"] == 'Bullish':
                    context['sentiment'] = 'positive'
                elif message["entities"]["sentiment"]["basic"] == 'Bearish':
                    context['sentiment'] = 'negative'

                dataset['data'].append(context)

        # construct new url
        new_url = url + '?max=' + str(data[-1]['id'] - 1)
        # request new data
        data = json.loads(requests.get(new_url).text)['messages']

    # save it to a json file
    with open('data/training_data.json', 'w') as outfile:
        json.dump(dataset, outfile)

# when the file is called, will update both tables and plots
if __name__ == "__main__":

    for ticker in dow30_tickers:
        updateTrainingData(ticker)
