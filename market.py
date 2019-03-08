from alpha_vantage.timeseries import TimeSeries
from config import av_api_key

# returns the percent change for the previous trading session of a stock
def getPercentChange(ticker):

    print("Processing", fullname, '(' + ticker + ')', "market activity")

    ts = TimeSeries(key='av_api_key', output_format='json')
    data, meta_data = ts.get_daily(symbol=ticker)

    close = float(list(data.values())[0]['4. close'])
    prev_close = float(list(data.values())[1]['4. close'])

    return (close - prev_close) / prev_close
