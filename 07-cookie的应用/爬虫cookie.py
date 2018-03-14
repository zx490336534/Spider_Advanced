from selenium import webdriver
import json
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get('https://weibo.cn/')
file = 'sina_cookies.txt'
with open(file,'r') as f:
    cookies = json.load(f)
    for cookie in cookies:
        cookie.pop('domain')
        driver.add_cookie(cookie)

driver.get('https://weibo.cn/?tf=5_009')
time.sleep(10)
driver.close()