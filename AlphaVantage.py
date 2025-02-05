# api key -- 87TXBXOXH79XVP3

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key = "87TXBXOXH79XVP3"

ts= TimeSeries(key,output_format="pandas")
data=ts.get_daily(symbol='MSFT',outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]
data=data.iloc[::-1]

all_tickers = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]

close_prices = pd.DataFrame()
api_call_count = 0
for ticker in all_tickers:
    start_time=time.time()
    ts=TimeSeries(key,output_format="pandas")
    data=ts.get_intraday(symbol=ticker,interbal='1min',outputsize='compact')[0]
    api_call_count+=1
    data.columns=["open","high","low","close","volume"]
    data=data.iloc[::-1]
    close_prices[ticker] = data['close']
    if api_call_count==5:
        api_call_count = 0
        time.sleep(60)

