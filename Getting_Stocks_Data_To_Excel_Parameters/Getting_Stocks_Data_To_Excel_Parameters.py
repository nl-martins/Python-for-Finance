import datetime as dt 
import pandas as pd
import pandas_datareader.data as web

"""
Validate the format of the date
d -> String with the date
Return True if the date is valid, False if not
"""
def validate_date(d):
    try:
        dt.datetime.strptime(d, '%d/%m/%Y')
        return True

    except ValueError:
        return False

""" MAIN """
#we ask the range of dates
start_string = str(input("Introduce start date (DD/MM/YYYY) :"))
while not validate_date(start_string) :
    start_string = str(input("Invalid. Introduce a date with the example format (31/12/2020) :"))

start_split = start_string.split('/')
start = dt.datetime(int(start_split[2]), int(start_split[1]) , int(start_split[0]))  #YEAR, MONTH, DAY 

end_string = str(input("Introduce end date (DD/MM/YYYY) :"))
while not validate_date(end_string) :
    end_string = str(input("Invalid. Introduce a date with the example format (31/12/2020) :"))

    end_split = end_string.split('/')
end = dt.datetime(int(end_split[2]), int(end_split[1]), int(end_split[0]))  #YEAR, MONTH, DAY 

saved = False
while not saved :
    ticker = str(input("Introduce the stock ticker:"))
    try:
        df = web.DataReader(ticker, 'yahoo', start, end)
        excel_name = str(input("Introduce a name for the excel file:"))
        df.to_excel(excel_name + '.xlsx')
        saved = True
    except Exception:
        print("Invalid ticker.")
