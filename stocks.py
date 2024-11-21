#! /usr/bin/env python3

#import the requried libraries
#Financial data
import yfinance as yf

#Dates and times
import datetime as dt#import the requried libraries
#Financial data
import yfinance as yf

#Dates and times
import datetime as dt

tickers = yf.Tickers('MSFT AAPL GOOG XRP')

df = yf.download(['MSFT', 'AAPL', 'GOOG'], period="1d", interval="1m")
#Get the current date and time
filename = dt.datetime.now()
#Create a string from the current date and time
filename = filename.strftime("%Y%m%d_%H%M%S")
#Prepend data folder, append file extension  
filename = 'data/' + filename + ".csv"
#Show the filename
filename

df['Close'].to_csv(filename)