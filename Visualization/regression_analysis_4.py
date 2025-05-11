import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2차 함수 그릴려고
from scipy.optimize import curve_fit

data = pd.read_table('income.txt')

# bug 78    3     NaN 와 같이 비어있는 자료가 존재하는 경우에는 데이터 행을 삭제하거나 값에다가 평균을 넣는게 일반적인듯
# info NaN 데이터 행 지우기
data = data.dropna()
print(data)

plt.scatter(data['age'], data['income'])
plt.show()

def function(x, a, b, c):
    return a*x + b*x**2 + c

# curve graph, opt : a, b, c 값, cov : 공분산
opt, cov = curve_fit(function, data['age'], data['income'])

print(opt)

a, b, c = opt

x = np.array([1, 2, 3, 4, 5, 6])

# info function(x, opt[0], opt[1], opt[2]) 넣어도 문제없음
plt.plot(x, function(x, a, b, c))
plt.scatter(data['age'], data['income'])
plt.show()