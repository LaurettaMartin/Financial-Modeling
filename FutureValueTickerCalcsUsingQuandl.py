import quandl
import math
import matplotlib.pyplot as plt
import pandas as pd


quandl.ApiConfig.api_key = 'zooLDBS17FRfzfSY5eUT'

ticker_input = input("Enter the ticker symbol: ")
site = "WIKI/"
stock_data = quandl.get(site + ticker_input)
present_value = stock_data['Close'][-1]
print("Present Value of {} is {}".format(ticker_input, present_value))



#FV of stock in 1 year
annual_return = stock_data['Close'].pct_change(periods = 252)
#approx 252 trading days in a given year
present_value = stock_data['Close'][-1]
years = 1
futureVal = present_value * (1 + annual_return) ** years
FV = futureVal[-1]
print("Future Value of {} is projected to be {} in 1 year.".format(ticker_input, FV))



#FV of stock in 3 years
annual_return = stock_data['Close'].pct_change(periods = 252)
#approx 252 trading days in a given year
present_value = stock_data['Close'][-1]
years = 3
futureVal = present_value * (1 + annual_return) ** years
FV = futureVal[-1]
print("Future Value of {} is projected to be {} in 3 years.".format(ticker_input, FV))



#FV of stock in 5 years
annual_return = stock_data['Close'].pct_change(periods = 252)
#approx 252 trading days in a given year
present_value = stock_data['Close'][-1]
years = 5
futureVal = present_value * (1 + annual_return) ** years
FV = futureVal[-1]
print("Future Value of {} is projected to be {} in 5 years".format(ticker_input, FV))



#Stock Price Plot
plt.plot(stock_data['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.title('{} Stock Price'.format(ticker_input))
plt.show()


