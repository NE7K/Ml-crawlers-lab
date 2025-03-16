from selenium import webdriver

# Keys = enter, ecs를 입력하고 싶을 때
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 복붙
import pyperclip

# chrome 내부에 정보 남기는용
from selenium.webdriver.chrome.options import Options

# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

optionTest = webdriver.ChromeOptions()
# user-data-dir 앞에 -- 꼭 넣어줘야 함
optionTest.add_argument(r'--user-data-dir=/Users/azullcarrot/Library/Application Support/Google/Chrome/Default')

driver = webdriver.Chrome(options=optionTest)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')

time.sleep(2)

# id .env에서 훔쳐오기
pyperclip.copy(os.getenv('id'))

id = driver.find_element(By.CSS_SELECTOR, '#id')
id.send_keys(Keys.COMMAND, 'v')

time.sleep(1)

# pw .env에서 훔쳐오기
pyperclip.copy(os.getenv('pw'))

pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.send_keys(Keys.COMMAND, 'v')

time.sleep(1)

pw.send_keys(Keys.ENTER)

input('enter')
