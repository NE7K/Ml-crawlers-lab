import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_table('income.txt')

# bug 78    3     NaN 와 같이 비어있는 자료가 존재하는 경우에는 데이터 행을 삭제하거나 값에다가 평균을 넣는게 일반적인듯
# info NaN 데이터 행 지우기
data = data.dropna()
print(data)

plt.scatter(data['age'], data['income'])
plt.show()