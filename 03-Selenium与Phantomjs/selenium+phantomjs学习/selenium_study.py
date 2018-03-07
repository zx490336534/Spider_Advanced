#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import time

from selenium.webdriver.common.by import By

__author__ = 'Terry'

# 浏览器的位置，相对路径，使用绝对路径也是可以的
phantomjs_driver_path = 'browser/phantomjs.exe'

from selenium import webdriver

# 启动驱动，不同的浏览器启用不同的类
driver = webdriver.PhantomJS(phantomjs_driver_path)

# 访问目标页面
driver.get('https://www.baidu.com')

# 下面有3种延时方式的展示，一般实际项目中不会同一个地方用3个延时，选择一个或多个使用

# 绝对延时，等待规定时间后，直接执行后面的代码
time.sleep(1)

# 隐性延时，最长是30秒，如果30秒内，资源全部加载完成，那么执行后续的代码，
# 30秒内没有加载完成，也会继续执行后续代码
# driver.implicitly_wait(30)

# 显性等待，等待时长20秒，间隔0.5秒去查询一次，目标元素是否加载完成
# 20秒内加载完成后，执行后续的代码，最长等待20秒，没有加载也会继续执行
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get('https://huilansame.github.io')
# locator = (By.LINK_TEXT, 'CSDN')
# WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

# 通过xpath的方式查找
su = driver.find_element_by_xpath('//*[@id="su"]')
# 通过标签的id查找
# driver.find_element_by_id()
# 通过标签的css选择器查找
# driver.find_element_by_css_selector()
# 通过class进行查找
# driver.find_element_by_class_name()

# 也是通过标签的xpath，等同于 driver.find_element_by_xpath('//*[@id="su"]')
# driver.find_element(By.XPATH, '//*[@id="su"]')

print(driver.title)
print(su.get_attribute('value'))

# 需要手动退出driver
# 切记切记一定退出
driver.quit()