# using regex
import re

# xlsx file open import
import pandas as pd

# 정규식 문자를 검사하는 식
save = re.search('Regex', 'Regex here')

# find all을 이용해서 중복 및 여러개를 찾고 list에 insert
save = re.findall('단어', '나는 아무 말도하지 않을 것이다. 어떠한 단어도')

# Regex : start word '^', end word '$' < 이러한 단어를 찾기 위해서는 '\'를 붙여야 검색 가능 
# a or b > [ab], [a-zA-Z]는 a부터 z까지 영어 대문자 A-Z
# 한글은 힣까지
# [^0-9] 0부터 9가 아닌 것, 모든 숫자를 나타내고 싶으면 \d, \d\d는 두 자리 숫자
# \d{3}은 \d를 3번 곱하는 것, \D는 숫자가 아닌 것, \s는 스페이스바가 아닌 것
# ㅋ+는 ㅋ이 반복되는 것을 다 가져옴

# re.IGNORECASE = 대소문자 구분 x
save = re.findall('단어', '나는 아무 말도하지 않을 것이다. 어떠한 단어도', re.IGNORECASE)

# date change regex
re.sub('이걸 찾아서', '이렇게 바꿔주세요', '이 문장을')
test = re.sub('\-', '.', '2025-01-01')

# Question 만약에 문장에서 숫자를 제거하고 싶으면
test = re.sub('\d', '', '이것은 문4장이3라2네')

# print(test)
# print(save)

# Question Q1. 이메일형식이 맞는지 판단하는 정규식을 만들어보십시오. = @이 뒤에 .이 오는지 찾아보고 리스트로 저장 = 
# 문자@문자.문자 - 정확히 문자인지 이어주는건? and
Q1 = re.findall('\S+@\S+.\S+', 'abc@example.com')
print(Q1)

# Question Q2. 상품목록에 Mirror 또는 Sofa라는 영단어가 포함되어있으면 카테고리컬럼에 '가구'라고 기록하고 싶습니다. 

# 1. 표 출력
test2 = pd.read_excel('product.xlsx', engine='openpyxl')
# print(test2)

# 2. def - if - Mirror and Sofa > insert '가구', a는 상품목록의 
def insert(a):
    # | > 또는 이라는 의미인듯
    if re.search('Mirror|Sofa', str(a)) : 
        return '가구'
    
# apply => 함수에 넣었다가 빼주세요
test2['카테고리'] = test2['상품목록'].apply(insert)

# print(test2)

# Question Q3. 상품목록에 글자가 없고 숫자만 있으면 그 칸은 '에러'라는 단어로 바꾸고 싶습니다. 

# 1. def - if - 상품 목록에 숫자는 Error로 대체
def tc_Error(a):
    # only number = Error, a라는 문장에 숫자가 아닌 문자가 있으면 return a 아니면 error return
    if re.search('\D', str(a)) :
        return a
    else :
        return 'Error'
    
test2['상품목록'] = test2['상품목록'].apply(tc_Error)

print(test2)