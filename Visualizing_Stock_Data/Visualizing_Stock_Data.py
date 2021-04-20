import datetime as dt 
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#we choose the range of dates
start = dt.datetime(1980,12,12) #IPO Date for APPLE
end = dt.date.today()

df = web.DataReader('AAPL', 'yahoo', start, end)

df['Adj Close'].plot()
plt.show()
