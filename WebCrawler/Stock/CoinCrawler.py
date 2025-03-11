import requests
import json
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/BTC?lastDt=1739977200000&interval=1H&1741416415785')

# print(data.content)

dict = json.loads(data.content)

for i in range(200):
    # time get [1739257200000] 뒤 3자리는 밀리세컨즈
    # print(dict['body']['candles'][i]['dt'])
    getTime = dict['body']['candles'][i]['dt']
    resultTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(getTime/1000))
    print(resultTime)
    print(dict['body']['candles'][i]['close'])
    
