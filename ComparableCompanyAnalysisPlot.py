import quandl
import pandas as pd
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "zooLDBS17FRfzfSY5eUT"
    
ticker1 = input("Enter the ticker symbol of Company 1: ")
ticker2 = input("Enter the ticker symbol of Company 2: ")
ticker3 = input("Enter the ticker symbol of Company 3: ")

comp1 = quandl.get("WIKI/{}".format(ticker1),start_date="2015-01-01", end_date="2021-12-31")
comp2 = quandl.get("WIKI/{}".format(ticker2),start_date="2015-01-01", end_date="2021-12-31")
comp3 = quandl.get("WIKI/{}".format(ticker3),start_date="2015-01-01", end_date="2021-12-31")

ccAverage = (comp1 + comp2 + comp3)/3

plt.plot(comp1['Close'], label='{}'.format(ticker1))
plt.plot(comp2['Close'], label='{}'.format(ticker2))
plt.plot(comp3['Close'], label='{}'.format(ticker3))
plt.plot(ccAverage['Close'], label='Comparable Companies Average Closing Price')

plt.legend()
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.title('{}, {}, and {} Closing Prices Including Industry Average'.format(ticker1, ticker2, ticker3))

# Show the plot
plt.show()

