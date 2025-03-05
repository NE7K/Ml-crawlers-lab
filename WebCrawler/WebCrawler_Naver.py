import urllib.request
# 이미지
import requests
# 웹 접속
from bs4 import BeautifulSoup
# 웹 문서 분석

# Samsung
dataSS = requests.get('https://finance.naver.com/item/sise.naver?code=005930')

# print(data.content)
# print(data.status_code)

resultSS = BeautifulSoup(dataSS.content, 'html.parser')

print('- SamSung -')

# 현재가
print(resultSS.find_all('strong', id="_nowVal")[0].text)

# 거래량
print(resultSS.find_all('span', id="_quant")[0].text)

# per (class로 찾기)
print(resultSS.find_all('span', class_="tah p11")[15].text)

# 동일업종 등락률
chart_image = resultSS.select('#img_chart_area')[0]

# 이미지 다운
# chart_url = chart_image['src']

# urllib.request.urlretrieve(chart_image['src'], '주가')

# LG
dataLG = requests.get('https://finance.naver.com/item/sise.naver?code=003550')

resultLG = BeautifulSoup(dataLG.content, 'html.parser')

print('- LG -')

# 현재가
print(resultLG.find_all('strong', id="_nowVal")[0].text)

# 거래량
print(resultLG.find_all('span', id="_quant")[0].text)

# per (class로 찾기)
print(resultLG.find_all('span', class_="tah p11")[15].text)

# 동일업종 등락률
chart_image = resultLG.select('#img_chart_area')[0]