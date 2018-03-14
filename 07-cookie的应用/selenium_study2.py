#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random

__author__ = 'Terry'

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'
]

phantomjs_driver_path = 'browser/phantomjs.exe'

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
# dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))
dcap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'


driver = webdriver.Chrome()

# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
driver.set_page_load_timeout(10)

# 设置10秒脚本超时时间
driver.set_script_timeout(10)

driver.maximize_window()

# 访问新浪移动端，没有验证码
driver.get('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginName"]')))

print(driver.title)

time.sleep(1)

user = driver.find_element_by_xpath('//*[@id="loginName"]')
# 清楚当前input元素中的值
user.clear()
# 在input元素中输入内容
use = input('use:')
user.send_keys(use)

pwd = driver.find_element_by_xpath('//*[@id="loginPassword"]')
pwd.clear()
passwd = input("pwd:")
pwd.send_keys(passwd)

login = driver.find_element_by_xpath('//*[@id="loginAction"]')
# 出发这个login元素的click事件
login.click()

WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, '//p[@data-node="title"]')))

print(driver.title)

title = driver.find_element_by_xpath('//p[@data-node="title"]')
print(title.text)

cookies = driver.get_cookies()
print(cookies)

# 需要手动退出driver
file = 'sina_cookies.txt'
with open(file,'w') as f:
    # 不建议：f.write(str(cookies))
    json.dump(cookies,f)


driver.quit()