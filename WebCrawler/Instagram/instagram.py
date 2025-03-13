from selenium import webdriver

# Keys = enter, ecs를 입력하고 싶을 때
from selenium.webdriver.common.keys import Keys

# by select 이용하려고 할 때
from selenium.webdriver.common.by import By
import time

# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

# 처음 세팅 시에는 비워두기
driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

# 코드 정지
time.sleep(2)

id = driver.find_elements(By.CSS_SELECTOR, 'input[name="username"]')
id[0].send_keys(os.getenv('id'))

passwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
passwd.send_keys(os.getenv('pw'))


# 버튼 상위 div > x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1
# 버튼 class  _acan _acap _acas _aj1- _ap30
# pressClick = driver.find_element(By.CSS_SELECTOR, '._acan button').click()
pressClick = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').send_keys(Keys.ENTER)

# page move / game tag search
# instagram.com/explore/tags/검색단어/ 이게 과거 주소인듯
time.sleep(4)
driver.get('https://www.instagram.com/explore/search/keyword/?q=%EA%B2%8C%EC%9E%84')

# 요소가 나올 때까지 기다려
driver.implicitly_wait(10)
e = driver.find_element(By.CSS_SELECTOR, '._aagu')
# script 이용해서 강제로 클릭
driver.execute_script('arguments[0].click();', e)


# 종료 방지
# input('enter')

time.sleep(20)
# driver.close()