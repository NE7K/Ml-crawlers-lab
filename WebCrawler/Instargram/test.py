import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 처음 세팅 시에는 비워두기
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/?flo=true')

driver.quit()