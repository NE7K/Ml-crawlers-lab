import pandas as pd

# 시계열 데이터 사용시 필요 import
import matplotlib.pyplot as plt

# finance data download
import yfinance as yf

test = yf.download('^GSPC', start='1999-01-01', end='2025-01-01')

# print(test)

# [x], [y] 축 데이터
plt.plot(test.index, test['Close'], color='crimson')

# x, y축 name 지정
plt.xlabel('time')
plt.ylabel('price($)')

# 범례 출력
plt.legend(['S&P 500'])

# title
plt.title('chart')

plt.show()