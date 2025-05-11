import requests

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('key')

# result = requests.GET인지POST인지('요청할URL', data=보낼데이터, headers=헤더스)
result = requests.post(
    'https://api-free.deepl.com/v2/translate',
    data={"text":["Hello, world!"],"target_lang":"DE"},
    headers={"Authorization": f"DeepL-Auth-Key {api_key}"})

# POST /v2/translate HTTP/2
# Host: api.deepl.com
# Authorization: DeepL-Auth-Key [yourAuthKey] 
# User-Agent: YourApp/1.2.3
# Content-Length: 45
# Content-Type: application/json

# {"text":["Hello, world!"],"target_lang":"DE"}

print(result.json())