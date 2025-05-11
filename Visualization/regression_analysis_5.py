import statsmodels.api as sm
import numpy as np
import pandas as pd

data = pd.read_table('income.txt')

data = data.dropna()

# np.ones(78) : 1이 78개 들어있는 리스트 넣을 수 있음
# 곡선이기 때문에 데이터를 ([[첫놈 나이, 첫놈 나이 제곱, 1], [둘째놈 나이, 둘째놈 나이 제곱, 1]])
# column stack : [[첫항목], [둘항목], [셋항목] ... ]

# FIX 여기서 const         -7.0077      9.126     -0.768      0.445     -25.184      11.169
# p>|t|가 0.4값이 나온 것을 확인할 수 있는데 상수를 빼서 회귀분석의 정확도를 올릴 수 있음
# x = np.column_stack([data['age'], data['age']**2, np.ones(79)])
x = np.column_stack([data['age'], data['age']**2])

# note 만약에 예측을 잘하고 싶어서 20차 함수로 만들어버리면 데이터 overfitting 현상이 발생함 (오히려 예측력이 떨어질 수 있음)
model = sm.OLS(data['income'],x).fit()
print(model.summary())