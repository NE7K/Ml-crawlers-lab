import requests
from bs4 import BeautifulSoup

# 종목 코드
dataList = ['005930', '066575', '005380', '035720', '034220', '003490']

def parse(StockNumber):
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={StockNumber}')
    result = BeautifulSoup(data.content, 'html.parser')
    result.find_all('strong', id="_nowVal")[0].text
    result.find_all('span', id="_quant")[0].text

    # 결과 반환 (현재값만 반환)
    return result.find_all('strong', id="_nowVal")[0].text

# 6번 함수 실행
for i in range(6):
    print(parse(dataList[i]))
    
# 파일 작성 모드로 오픈 
f = open('CrawlerResult.txt', 'w')

# 6번 함수 실행 및 저장
for i in dataList:
    f.write(parse(i) + '\n')

f.close()