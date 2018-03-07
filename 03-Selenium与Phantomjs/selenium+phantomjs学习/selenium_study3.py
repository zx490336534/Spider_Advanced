#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

def save_vcode(driver, element):
    # 获取截图
    driver.get_screenshot_as_file('screenshot.png')

    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])

    # 通过Image处理图像
    from PIL import Image
    im = Image.open('screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('vcode.png')

dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
# dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))
dcap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'

# 不载入图片，爬页面速度会快很多
# dcap["phantomjs.page.settings.loadImages"] = False

#打开带配置信息的phantomJS浏览器
driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap)

# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
driver.set_page_load_timeout(10)

# 设置10秒脚本超时时间
driver.set_script_timeout(10)

# 设置屏幕尺寸
driver.set_window_size(1366, 768)

# 访问百度
driver.get('https://www.baidu.com')

WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="u1"]/a[7]')))

print(driver.title)

time.sleep(1)

# 点击 弹出登录的窗口
login_index = driver.find_element_by_xpath('//*[@id="u1"]/a[7]')
login_index.click()

time.sleep(.5)

# 选择 用户名登录
login_user_and_pwd = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]')
login_user_and_pwd.click()

time.sleep(.5)

# 用户名元素
user = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]')
user.clear()
user.send_keys('mumuloveshine')

# 密码元素
pwd = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]')
pwd.clear()
pwd.send_keys('mumu2018')

while True:
    # 换下一张 验证码
    next_vcode = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__verifyCodeChange"]')
    next_vcode.click()
    # 验证码图片的元素
    vcode_img = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__verifyCodeImg"]')
    save_vcode(driver, vcode_img)

    # 输入验证码
    vcode_input = input('请输入验证码：')
    vcode = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__verifyCode"]')
    # 在页面上填写验证码
    vcode.send_keys(vcode_input)

    # 登录
    login = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]')
    login.click()

    time.sleep(1)

    try:
        # 判断是否登录成功
        user_name = driver.find_element_by_xpath('//*[@id="s_username_top"]/span')
        print("登录名为："+user_name.text)
        print("登录成功：")
        break
    except:
        time.sleep(.3)

driver.get('http://index.baidu.com/?tpl=trend&word=%BB%C6%BD%F0')

# 需要手动退出driver
driver.quit()