import pandas as pd

# info pip install yfinance : api 서비스 지원 종료로 새로운 api 사용
import yfinance as yf

# bug install pandas_datareader | stock data 
from pandas_datareader import data

# bug get data, ('', '') : stock number | stock api site [yahoo api]
# test = data.DataReader('AAPL', 'yahoo', start="2019-01-01", end="2020-01-01")

# print(test)

# using yf
test = yf.download('AAPL', start="2019-01-01", end="2020-01-01")

print(test)