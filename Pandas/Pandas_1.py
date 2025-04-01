import pandas as pd

test = pd.read_csv('credit.csv')

# # note pandas 라이브러리를 사용해서 자료를 뽑을 때 딕셔너리 뽑듯이 사용할 수 있음
# # info age data average
# print(test['나이'].mean())

# # info age data 최빈값
# print(test['나이'].mode())

# # info age data max and min result
# print(test['나이'].max())
# print(test['나이'].min())

# # info data 분석 간단 명령어
# print(test['나이'].describe())

# bug numeric_only=True 숫자 컬럼만 가져오기 < 이거 안쓰면 오류남
# print(test.groupby('성별').mean(numeric_only=True))

# info 2개 컬럼의 관계
# context = test[['나이', '사용금액']].corr()

context = test[ test['나이'] > 50 ]

print(context)