import urllib.request
# 이미지
import requests
# 웹 접속
from bs4 import BeautifulSoup
# 웹 문서 분석

# # Samsung
# dataSS = requests.get('https://finance.naver.com/item/sise.naver?code=005930')

# # print(data.content)
# # print(data.status_code)

# resultSS = BeautifulSoup(dataSS.content, 'html.parser')

# print('- SamSung -')

# # 현재가
# print(resultSS.find_all('strong', id="_nowVal")[0].text)

# # 거래량
# print(resultSS.find_all('span', id="_quant")[0].text)

# # per (class로 찾기)
# print(resultSS.find_all('span', class_="tah p11")[15].text)

# # 동일업종 등락률
# chart_image = resultSS.select('#img_chart_area')[0]

# 이미지 다운
# chart_url = chart_image['src']

# urllib.request.urlretrieve(chart_image['src'], '주가')

# yahoo finance nasdaq 100
# dataLG = requests.get('https://finance.yahoo.com/quote/NQ%3DF/')

# resultLG = BeautifulSoup(dataLG.content, 'html.parser')

# print('- 나스닥 100 -')

# # 현재가
# print(resultLG.find_all('strong', id="_nowVal")[0].text)

# # 거래량
# print(resultLG.find_all('span', id="_quant")[0].text)

# per (class로 찾기)
# print(resultLG.find_all('span', class_="base down1   yf-ipw1h0"))

# 동일업종 등락률
# chart_image = resultLG.select('#img_chart_area')[0]

# 종목 코드
dataList = ['005930', '066575', '005380', '035720', '034220', '003490']

# 리턴 기록 넣어두는 곳
resultData = []

# 함수를 만들어줘야지 ㅋㅋ
def crawle(StockNumber):
    # f = 포멧팅
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={StockNumber}')
    result = BeautifulSoup(data.content, 'html.parser')
    result.find_all('strong', id="_nowVal")[0].text
    result.find_all('span', id="_quant")[0].text

    # return result.find_all('strong', id="_nowVal")[0].text
    return result.find_all('strong', id="_nowVal")[0].text

    # dataList.append()
    # resultData.append(result.find_all('strong', id="_nowVal")[0].text)

# 함수 실행 / resultData[i]에 길이만큼 함수 실행하고 저장
for i in range(dataList):
    resultData[i] = crawle(dataList[i])
    

# 실행 함수들 자료 저장 및 파일화
f = open('CrawlerResult.txt', 'w')

# 모든 종목 코드를 그 안에다 출력
for i in range(resultData):
    f.write(resultData[i])
    
# for i in range(0, 2):
#     f.write(resultData[i])
f.close()