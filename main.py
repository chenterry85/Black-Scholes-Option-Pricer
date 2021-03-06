from time import time
from black_schole import call_price, call_implied_volatility, put_price
from datetime import datetime, date
import pandas_datareader.data as web
import numpy as np

stock = 'SPY'
expiry = '12-18-2022'
strike_price = 420

today = datetime.utcnow()
# moving today back a month due to 7/4 holiday (stock market closed)
today = today.replace(month=today.month-1)
one_year_ago = today.replace(year=today.year-1)

df = web.DataReader(stock, 'yahoo', one_year_ago, today)
df = df.sort_values(by="Date")
df = df.dropna()
df['close_day_before'] = df['Close'].shift(1) # create new column "close_day_before"
df['returns'] = ((df['Close'] - df['close_day_before']) / df['close_day_before'])
# find volatility of stock (# of market open days = 251)
sigma = np.sqrt(252) * df['returns'].std()

# find 10-year US Treasury bond as risk-free rate
risk_free_rate = (web.DataReader(('^TNX'), 'yahoo', today.replace(day=today.day-2), today)['Close'].iloc[-1]) / 100.
current_price = df['Close'].iloc[-1]
time_to_expiry = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365.

print("Find Volatility: ", call_implied_volatility(1, 100, 120, 0.05, 30/365.))