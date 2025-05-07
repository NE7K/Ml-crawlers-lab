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

# test2 = yf.download('AMZN', start='2020-01-01', end='2020-12-31')

# test2['rolling-20'] = test2['Close'].rolling(20).mean()
# test2['rolling-60'] = test2['Close'].rolling(60).mean()

# plt.plot(test2.index, test2['Close'])
# plt.plot(test2.index, test2['rolling-20'])
# plt.plot(test2.index, test2['rolling-60'])

# plt.show()

# Question Q2. 삼성전자와 경쟁업체 LG전자의 매출 데이터는 다음과 같습니다. 
# 팀장님이 이걸 이쁜 그래프로 만들어서 보고를 올리라고 하는군요.
# 그러니 matplotlib을 이용해 이쁘게 그려보십시오. 팀장님은 연세가 있어 x,y축 라벨과 legend도 친절하게 적어드려야합니다.

Samsung = [50000, 60000, 75000, 70000]
LG = [30000, 40000, 50000, 35000]
Date = [2018, 2019, 2020, 2021]

plt.plot(Date, Samsung)
plt.plot(Date, LG)

plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(['Samsung', 'LG'])

plt.show()