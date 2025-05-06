import pandas as pd

# info matplotlib : pip install matplotlib 시각화 라이브러리
import matplotlib.pyplot as plt

# info pip install yfinance : api 서비스 지원 종료로 새로운 api 사용
import yfinance as yf

# bug install pandas_datareader | stock data 
from pandas_datareader import data

# bug get data, ('', '') : stock number | stock api site [yahoo api]
# test = data.DataReader('AAPL', 'yahoo', start="2019-01-01", end="2020-01-01")

# print(test)

# using yf
# test = yf.download('AAPL', start="2019-01-01", end="2020-01-01")

# plot() : graph
# test['Close'].plot()

# info Visualization data terminal
# plt.show()

# 국내 stock price
# test2 = data.DataReader('005930', 'naver', start="2019-01-01", end="2020-01-01")

# dtype : object > 타입 변환은 astpye(int or float 등등)
# test2['Close'] = test2['Close'].astype(float)
# test2['Close'].plot()

# plt.show()
# dataframe에는 index 존재가능, 현재와 같은 경우는 왼쪽에 있는 데이터가 date data기 때문에 index처럼 번호를 매겨줌
# print(test2.index)

# S&P 500 or nasdaq code = ^GSPC, ^NDX

test3 = yf.download('^NDX', start="2020-01-01", end="2025-01-01")

# rolling 120개씩 묶고 mean()으로 평균, sum()은 합계
test3['rolling120'] = test3['Close'].rolling(120).mean()
test3['rolling60'] = test3['Close'].rolling(60).mean()

test3['Close'].plot()
test3['rolling120'].plot()
test3['rolling60'].plot()

plt.show()