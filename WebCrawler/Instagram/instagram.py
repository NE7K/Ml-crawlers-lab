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
time.sleep(5)

id = driver.find_elements(By.CSS_SELECTOR, 'input[name="username"]')
id[0].send_keys(os.getenv('id'))

passwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
passwd.send_keys(os.getenv('pw'))

# pressClick = driver.find_element(By.CSS_SELECTOR, '._acan button').text
# print(pressClick)


# x1anpbxc x1h5jrl4 xyorhqc xmn8rco => div class에 있는 span 찾기
# e = driver.find_element(By.CSS_SELECTOR, '.x1anpbxc span').text
# print(e)

# getInput = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
# print(getInput.text)

# 종료 방지
input('enter')
# driver.close()