#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = 'Terry'

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
]

phantomjs_driver_path = 'browser/phantomjs.exe'

from selenium import webdriver
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))

# 不载入图片，爬页面速度会快很多
# 这一步大家一定要小心，连验证码都不会下载的！！！！！！！！！
dcap["phantomjs.page.settings.loadImages"] = False

# 设置代理
# service_args = ['--proxy=127.0.0.1:8888','--proxy-type=https']
# service_args = []

#打开带配置信息的phantomJS浏览器
# driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap, service_args=service_args)
driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap)

# 隐式等待5秒，可以自己调节
# driver.implicitly_wait(5)

# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
driver.set_page_load_timeout(10)

# 设置10秒脚本超时时间
driver.set_script_timeout(10)

# 设置cookie
# driver.add_cookie({'name': 'key', 'value': 'value', 'path': '/'}) # 会报错
# driver.add_cookie({'name': 'key', 'value': 'value', 'domain': '.baidu.com'}) # 会报错
driver.add_cookie({'name': 'key', 'value': 'value', 'domain': '.baidu.com', 'path': '/'})

driver.get('https://www.baidu.com')

su = driver.find_element_by_xpath('//*[@id="su"]')
su1 = driver.find_element_by_id('su')

from selenium.webdriver.common.by import By
su2 = driver.find_element(by=By.ID, value="su")

print(su.get_attribute('value'))
print(su1.get_attribute('value'))
print(su2.get_attribute('value'))

# 执行js脚本 ,execute_script可以执行任意的正确的js代码, 运行环境是当前的页面环境
driver.execute_script('document.getElementById("su").value="百度二下"')
su3 = driver.find_element_by_id('su')
print(su3.get_attribute('value'))

# 需要手动退出driver
driver.quit()