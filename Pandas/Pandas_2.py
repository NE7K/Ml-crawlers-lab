import pandas as pd

# 정규화 사용 import
import re

# note excel file open => read 'exel', engine='openpyxl'
df = pd.read_excel('product.xlsx', engine='openpyxl')

# 컬럼 추가하고 print해줘야지 추가가되는거 같음
# df['부가세포함'] = df['판매가'] * 1.1

# function에 매개변수 담아서 출력해보기
# def function(a):
#     return a * 1.1

# print(df['판매가'].apply(function))

# print(df)

# info re.search('정규식', '데이터') 왼쪽의 데이터가 오른쪽에 있는지 찾아주세요
# note ^정규식 = 정규식으로 시작하는 데이터 ex) ^abc, abc~~
def typeCategorie(a):
    if re.search('Chair', str(a)):
        return 'Chair'
    if re.search('Table', str(a)):
        return 'Table'
    
# Question 상품목록에 따른 카테고리 부여
df['카테고리'] = df['상품목록'].apply(typeCategorie)

print(df)