from sklearn import metrics
import tensorflow as tf

import pandas as pd

data = pd.read_csv('gpascore.csv')

# info null 값 찾기, fillna는 채우는거 .mean
# print(data.isnull().sum())
data = data.dropna()
# print(data.isnull().sum())
# data['~'].min(), max, count

result = data['admit'].values
xdata = []

# data get
for i, rows in data.iterrows():
    print(rows)

# 잠시 아래 실행 안 함
exit()

# 이거쓰면 자동으로 신경망 레이어 만들어줌 ㄷㄷ
model = tf.keras.models.Squential([
    # hidden layer insert number은 2의 제곱으로 관습적으로 사용
    # info activation list sigmoid, tanh, relu, softmax
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    # last node는 1개
    # info sigmoid 0~1
    tf.keras.layers.Dense(1, activation='sigmoid'),    
])

# optimizer : 기울기를 구해서 뺀다고 했는데, 빼는 값을 조정
# loss : 상황에 맞는 loss 함수가 정해져 있음 binary_crossentropy는 0과 1사이 분류/확률문제에서 씀
# metrics : 모델을 딥러닝할때 어떤 요소를 평가할 것인지
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x, y, epochs=10)