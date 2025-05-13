import matplotlib.pyplot as plt

# list include list library
import numpy as np

# analysis library
from sklearn.linear_model import LinearRegression

# np.array and .reshape((-1, 1))로 LinearRegression에서 요구하는 자료 형태 만족
size = np.array([170,180,160,165,158,176,182,172]).reshape((-1, 1))
weight = [75,81,59,70,55,78,84,72]

plt.scatter(size, weight)
# plt.show()

# info OLS(Ordinary Least Squares)를 충족하는 선을 그리면 예측할 수 있음
# 이 선을 그리는 방법은 scatter chart 점과 선의 거리가 적은 것을 찾으면된다
# 주의점으로는 오차를 제곱을해서 더해야 한다는 점 (오차가 음수가 나올 수 있기 때문)

# create model, fit(x, y) x와 y는 키값
model = LinearRegression().fit(size, weight)

# R (0~1)의 제곱 R 값이 0에 가까이 갈수록 관련이 없다는 것, 1에 가까이 갈수록 관련이 있다는 것
print(model.score(size, weight))
# y = ax + b 중에서 b값
print(model.intercept_)
# y = ax + b 중에서 a값
print(model.coef_)

# info 즉, y = 1.1x -118
# x값 데이터를 넣었을 때 결과값
test = model.predict([[183]])
print(test)

# 최적의 선
plt.plot(size, model.predict(size))
plt.show()