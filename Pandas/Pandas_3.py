import re

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

print(test)
print(save)