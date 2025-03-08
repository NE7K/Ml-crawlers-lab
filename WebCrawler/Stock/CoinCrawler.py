import requests
import json

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/BTC?lastDt=1739977200000&interval=1H&1741416415785')

# print(data.content)

dict = json.loads(data.content)
print(dict['body']['candles'][0]['close'])
