# Quant
git add yfinance_test.py
git status
git commit -m "checking new file"
git push


-------------

Moving average ==> normal mean of past closing price
exponential average ==> gives higher weighty to recent. old data gets decayed.

MACD == moving avg convergence divergence
difference of 2 moving avg slow vs fast (ex 12 vs 26 )
then take moving avg (9 days) of above MACD line which is called signal line.
if MACD line cut signal line from below signal bullist period
if from above then called bearish period.


Bollinger bands - 2 lines plotted for 2 standard deviation and a simple moving avg line.
Band widen during increased volatility and shrink in low volatility.

ATR (Avg true range) have 3 range
   -- difference of high and low of each period
   -- high and prev period close
   -- low and prev period close


RSI - RElative strength index
This is a momentum oscillatior. value between 0 to 100. ABove 100 is overbought . Below 30 is oversold.

Renko- 


ADX ==> Average directional index
Strength of trend
0-25 ==> Weak trend
75-100 strong trend 




Links to sources discussed in the lecture videos

TA-Lib website: http://ta-lib.org/
TA-Lib Python Wrapper Github Page: https://mrjbq7.github.io/ta-lib/
TA-Lib documentation of pattern recognition: https://mrjbq7.github.io/ta-lib/func_groups/pattern_recognition.html
Discussion on installation problems: https://github.com/mrjbq7/ta-lib/issues/127
Command to install TA-lib for python 3.5 and 3.6: pip install -i https://pypi.anaconda.org/masdeseiscaracteres/simple ta-lib
Good website on chart patterns: http://thepatternsite.com

Use a dictionary (dict) for quick lookups, nested data, configurations, and JSON data.
Use a DataFrame (pandas.DataFrame) for structured data, filtering, and analysis.
Sometimes, you use both tog
ether—load data as a dictionary and convert it into a DataFrame for processing.
