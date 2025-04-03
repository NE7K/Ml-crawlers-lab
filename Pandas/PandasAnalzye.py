import pandas as pd

df = pd.read_csv('credit.csv')

print(df)

# Question : 결혼한 남자는 결혼 안한 남자에 비해 사용금액이 평균적으로 높은가?
# Q1 = df.query(" 성별 == 'M' and 기혼 == 'Married' ")['사용금액'].mean()
Q1 = df.query(" 성별 == 'M' and 기혼 == 'Married' ").mean(numeric_only=True)
print(Q1)

# Question : 소득이 높을 수록 사용금액이 평균적으로 높은가?
Q2 = df.groupby('소득').mean(numeric_only=True)
print(Q2)