import deepl

import os

# 자동으로 env 파일 불러오는 import
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('key')

auth_key = api_key  # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="KO")
print(result.text)  # "Bonjour, le monde !"