import datetime as dt 
import pandas as pd
import pandas_datareader.data as web

#we choose the range of dates
#IPO Date for APPLE
start = dt.datetime(1980,12,12) 
end = dt.date.today()

#reads the historical information and creates a DataFrame with it
df = web.DataReader('AAPL', 'yahoo', start, end)

#Creates an Excel with the Dataframe info
df.to_excel('AAPL_historical_price.xlsx')
