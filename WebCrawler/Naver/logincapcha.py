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

# notebook 환경에서는 wifi로 인해서 느릴 수 있으니 3초 지연주는 것이 안정적
# time.sleep(3)
# 혹은 implicitly wait 사용해서 요소가 나올 때까지 10초 동안 기다리도록 설정
driver.implicitly_wait(10)

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

# blog post move step 1
driver.get('https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0')

driver.implicitly_wait(10)

# blog post move step 2
driver.get(f'https://blog.naver.com/{os.getenv("id")}?Redirect=Write&')

# post context part
driver.implicitly_wait(10)

pyperclip.copy(os.getenv('headContext'))

# blog insert user context
headerData = driver.find_element(By.CSS_SELECTOR, 'div[data-a11y-title="제목"] span')
driver.send_keys(Keys.COMMAND, 'v')

time.sleep(1.5)

pyperclip.copy(os.getenv('mainContext'))

headerData = driver.find_element(By.CSS_SELECTOR, 'div[data-a11y-title="본문"] span')
driver.send_keys(Keys.COMMAND, 'v')


# blog post step 4 > 버튼 찾아서 발행 누르셈 ㅇㅇ

# class="header__Ceaap" 이거 헤더

# try:
#     # class="publish_btn__m9KHH" button[type="button"]
#     click = driver.find_element(By.CSS_SELECTOR, '.publish_btn_area__KjA2i')
# except Exception as e:
#     print(e)

input('enter')