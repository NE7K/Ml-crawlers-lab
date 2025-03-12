import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# 처음 세팅 시에는 비워두기
driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

# 코드 정지
time.sleep(2)
e = driver.find_element(By.CSS_SELECTOR, '.x1lliihq')
print(e)

# 종료 방지
input('enter')
driver.close()