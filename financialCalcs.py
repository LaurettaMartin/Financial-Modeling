import yfinance as yf
import pandas as pd
import matplotlib.pyplot as py

ticker = input("Provide a ticker symbol: ")
stock_data = yf.Ticker(ticker)

info = stock_data.info

historical_data = stock_data.history(period="1d", interval="1m")
historical_dataMax = stock_data.history(period="max", interval="1m")

financials = stock_data.financials
balance_sheet = stock_data.balance_sheet
cash_flow = stock_data.cashflow
earnings = stock_data.earnings
recommendations = stock_data.recommendations
holders = stock_data.institutional_holders
options_expirations = stock_data.options

writer = pd.ExcelWriter("{}companyOverview.xlsx".format(ticker), engine='xlsxwriter')

industry = stock_data.info['sector']
print("Sector: {}".format(industry))

# metrics
price = stock_data.info['regularMarketPrice']
print("Price: {}".format(price))
eps = stock_data.info['trailingEps']
print("Earnings Per Share: {}".format(eps))
dividend_yield = stock_data.info['dividendYield']
print("Dividend Yield   : {}".format(dividend_yield))

# ratios

pe_ratio = price/eps
print("PE Ratio: {}".format(pe_ratio))

# total_debt = stock_data.info['totalDebt']
# shareholder_equity = stock_data.info['totalStockholderEquity']
# de_ratio = total_debt / shareholder_equity
# print(de_ratio)




# competitors

# competitors = stock_data.recommendations['regularMarketPeers']
# print(competitors)

# trading data
cap = stock_data.info["marketCap"]
print("Market Cap: {}".format(cap))
vol = stock_data.info["volume"]
print("Volume: {}".format(vol))
avgVol = stock_data.info["averageVolume"]
print("Average Volume: {}".format(avgVol))
day10Vol = stock_data.info["averageVolume10days"]

financials_df = pd.DataFrame(financials)
financials_df.to_excel(writer, sheet_name='Financials')

balancesheet_df = pd.DataFrame(balance_sheet)
balancesheet_df.to_excel(writer, sheet_name='Balance Sheet')

cashflow_df = pd.DataFrame(cash_flow)
cashflow_df.to_excel(writer, sheet_name='Cash Flow')

# net_income = stock_data.info['forwardNetIncome']
# shareholder_equity = stock_data.info['regularMarketEquity']
# roe = net_income / shareholder_equity
# print(roe)

# roe = financials['NetIncome']['ttm']['fmt'] / balance_sheet['TotalShareholderEquity']['fmt']
# de_ratio = balance_sheet['TotalLiabilities']['fmt'] / balance_sheet['TotalShareholderEquity']['fmt']

# print("P/E ratio:", pe_ratio)
# print("Dividend yield:", dividend_yield)
# print("ROE:", roe)
# print("D/E ratio:", de_ratio)

earnings_df = pd.DataFrame(earnings)
earnings_df.to_excel(writer, sheet_name='Earnings')

recc_df = pd.DataFrame(recommendations)
recc_df.to_excel(writer, sheet_name='Recommendations')

holders_df = pd.DataFrame(holders)
holders_df.to_excel(writer, sheet_name='Holders')

opex_df = pd.DataFrame(options_expirations)
opex_df.to_excel(writer, sheet_name='Options Expirations')

# opt = stock_data.option_chain(date='2023-06-16')
# calls = opt.calls
# calls_df = pd.DataFrame(calls)
# opex_df.to_excel(writer, sheet_name='Calls Data')

# puts = opt.puts
# puts_df = pd.DataFrame(puts)
# opex_df.to_excel(writer, sheet_name='Puts Data')
writer.save()




#Conditionals

