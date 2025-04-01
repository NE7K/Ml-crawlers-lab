import pandas as pd

test = pd.read_csv('credit.csv')

# note pandas 라이브러리를 사용해서 자료를 뽑을 때 딕셔너리 뽑듯이 사용할 수 있음
# info age data average
print(test['나이'].mean())

# info age data 최빈값
print(test['나이'].mode())

# info age data max and min result
print(test['나이'].max())
print(test['나이'].min())

print(test['나이'].describe())