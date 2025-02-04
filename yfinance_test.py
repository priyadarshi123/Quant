import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

stocks  = ["AMZN","MSFT","META","GOOG"]
start = dt.datetime.today() - dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()   ##Dataframe to store closing price

ohlcv_data = {}  ## Empty dictionary filled with dataframe

for ticker in stocks:
    cl_price[ticker]= yf.download(ticker,start,end)["Close"]
    #print(cl_price)

print(cl_price)

print("wait.......")

#fill NaN values


#cl_price = cl_price.fillna({"AMZN":0 , "MSFT": 0, "3988.HK": 0})
#cl_price.fillna(method='ffill',axis=0,inplace=True)

#print(cl_price)

#dropping Nan values

cl_price.dropna(axis=0,inplace=True,how='any')

print(cl_price)

#cl_price.describe()

daily_return = cl_price.pct_change()
#print(cl_price/cl_price.shift(1) - 1) #same as above

#print(daily_return.mean())
#print(daily_return.std())

#print(daily_return.rolling(window=10).mean())   ## rolling window of 10 is created with same weightage for all weights.

#print(daily_return.ewm(com=10).mean())  ## exponential decay . so recent one given more weightage

#cl_price.plot(subplots=True,layout=(2,2),title="Stock Price Evolution")

#plt.show()

#(1+daily_return).cumprod().plot()  ## tell cumulative product of return # 100 * 1.1*1.01*1.05

#plt.show()

#Link to the blog referenced in the lecture video:

#https://pbpython.com/effective-matplotlib.html


#Matplotlib Tutorial:

#https://matplotlib.org/tutorials/introductory/lifecycle.html


fig, ax = plt.subplots()


ax.set(title='Mean daily return of stocks', xlabel = 'Stocks', ylabel = 'Mean REurn')
print(plt.style.available)  # to see avaialble style
plt.style.use("ggplot")
plt.bar(x=daily_return.columns,height=daily_return.mean())
#plt.bar(x=daily_return.columns,height=daily_return.std())
plt.show()