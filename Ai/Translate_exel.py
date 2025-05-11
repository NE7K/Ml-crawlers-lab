import os
from dotenv import load_dotenv
import pandas as pd
import deepl

load_dotenv()

api_key = os.getenv('key')

# FIX engine='openpyxl' 이거 안 넣어도 작동된단다 어메이징
data = pd.read_excel('english.xlsx', engine='openpyxl')

# print(data['english'])

# Question 하단에 첨부된 엑셀 파일에 있는 영어 문장들을 번역해서 새로운 엑셀 파일로 다시 뱉어봅시다.
# - 엑셀파일은 pandas로 읽을 수 있습니다.
# - 아마 DeepL API 문서 잘 보면 한 번에 여러 문장을 번역요청 날릴 수도 있긴 합니다.

auth_key = api_key  # Replace with your key
translator = deepl.Translator(auth_key)

data['korean'] = translator.translate_text(data['english'], target_lang="KO")

# note 함수에 넣어서 http get 씀 그리고 json으로 퉤
# def 번역하기(a):
#   url = 'https://api-free.deepl.com/v2/translate'
#   body = {'text': a, 'target_lang' : 'KO'}
#   headers = {'Authorization': 'DeepL-Auth-Key a6f15a47-7be6-46cd-97f2-bb50e96bb1ab:fx'}
#   result = requests.post(url, data=body, headers=headers)
#   return result.json()

# note .tolist() 일반 series 데이터를 python list data로 변환
# english_list = data['english'].tolist()
# note 함수에 집어 넣었다가 결과물 result에 삽입
# result = 번역하기(english_list)

# info l은 현재 행의 index data, row는 현재 행의 series data
# for l,row in data.iterrows():
# note data.loc[0, 'korean'] = '안녕하세요'
#   data.loc[l,'korean'] = result['translations'][l]['text']


print(data)
# 퉤
data.to_excel('output.xlsx')