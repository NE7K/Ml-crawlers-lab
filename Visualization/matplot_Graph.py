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

# Samsung = [50000, 60000, 75000, 70000]
# LG = [30000, 40000, 50000, 35000]
# Date = [2018, 2019, 2020, 2021]

# plt.plot(Date, Samsung)
# plt.plot(Date, LG)

# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.legend(['Samsung', 'LG'])

# plt.show()

# Question Q3. 원하는 데이터만 보이게 그래프를 조작하고 싶습니다. 
# yahoo에서 2020년 01월01일~12월31일의 비트코인 가격을 가져오고 Close 가격을 그래프로 그리고 싶습니다. (종목코드 BTC-USD)
# 근데 Volume항목 2020년의 평균Volume보다 높은 날의 가격만 그래프로 그려보고 싶은데 어떻게 코드를 짜야할까요? 

test3 = yf.download('BTC-USD', start='2020-01-01', end='2020-12-31')

# note index 작동 여부 확인
# print(test3.index)

# note test3['Close'] 작동 여부 확인
# print(test3['Close'])

# note volum 작동 여부 확인
# print(test3['Volume'])

# info if (test3['Volume].mean()<2020년도의 평균 볼륨보다 높은 날만 표시되게)

# 2020년도의 평균 거래량 : 3.298565e+10
avg = test3['Volume'].mean()

# 저장된 평균으로 T, F 구분
test3['new'] = test3['Volume'] > avg

# test3['new]에 저장된 데이터 중에서 True만 끄집어내서 pr에 저장
pr = test3[test3['new']==True]
print(pr)

# 멀티 인덱스로 인해서 ['BTC-USD'] 추가해줘야함
plt.bar(pr.index, pr['Close']['BTC-USD'])
plt.show()