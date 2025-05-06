import pandas as pd

# 시계열 데이터 사용시 필요 import
import matplotlib.pyplot as plt

# finance data download
import yfinance as yf

# test = yf.download('^GSPC', start='1999-01-01', end='2025-01-01')

# print(test)

# [x], [y] 축 데이터
# plt.plot(test.index, test['Close'], color='crimson')

# info bar chart : plt.bar(), pie chart : plt.pie([], label=['', '' ]), hist chart : plt.hist([''])

# x, y축 name 지정
# plt.xlabel('time')
# plt.ylabel('price($)')

# 범례 출력
# plt.legend(['S&P 500'])

# title
# plt.title('chart')

# info scatter chart
# math = [2, 33, 23, 99, 19, 98, 26]
# eng = [56, 78, 44, 31, 21, 33, 99]

# plt.scatter(math, eng)

# note chart size
# plt.figure(figsize=(10,10))
# info stackplot chart
# plt.stackplot([1,2,3], [10, 20, 30], [30, 20, 50], [50,10, 30])
# plt.show()

# Question Q1. 아마존 (종목코드 AMZN) 주식의 2020년 01월01일~12월31일 주식가격을 yahoo에서 가져온 후 20일, 60일 이동평균선을 그려보십시오.

test2 = yf.download('AMZN', start='2020-01-01', end='2020-12-31')

test2['rolling-20'] = test2['Close'].rolling(20).mean()
test2['rolling-60'] = test2['Close'].rolling(60).mean()

plt.plot(test2.index, test2['Close'])
plt.plot(test2.index, test2['rolling-20'])
plt.plot(test2.index, test2['rolling-60'])

plt.show()