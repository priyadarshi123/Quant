# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

tickers  = ["AMZN","MSFT","GOOG"]
start = dt.datetime.today() - dt.timedelta(36)
end = dt.datetime.today()
cl_price = pd.DataFrame()   ##Dataframe to store closing price

ohlcv_data = {}  ## Empty dictionary filled with dataframe

for ticker in tickers:
    temp= yf.download(ticker,period="1mo",interval="15m")
    #print(cl_price)
    # dropping Nan values
    temp.dropna(axis=0, inplace=True, how='any')
    ohlcv_data[ticker] = temp


#df=ohlcv_data["AMZN"]

def ATR(DF, n=14):
    df=DF.copy()
    df["H-L"] = df["High"]- df["Low"]
    df["H-PC"]=df["High"]-df["Close"].shift(1)
    df["L-PC"] = df["Low"] - df["Close"].shift(1)
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False)
    df["ATR"]=df["TR"].ewm(com=n,min_periods=n).mean()
    return df["ATR"]


for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATR(ohlcv_data[ticker])
