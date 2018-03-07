from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

#输入账号密码
myuser = input('输入账号：')
mypasswd = input('输入密码:')

driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com')
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(8)
login = driver.find_element_by_css_selector('#u1 > a.lb')
login.click()
driver.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn').click()
user = driver.find_element_by_css_selector('#TANGRAM__PSP_10__userName')
user.clear()
user.send_keys(myuser)
passwd = driver.find_element_by_css_selector('#TANGRAM__PSP_10__password')
passwd.clear()
passwd.send_keys(mypasswd)
driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit').click()
time.sleep(1)
driver.find_element_by_css_selector('#TANGRAM__PSP_10__verifyCodeChange').click() #换一张
time.sleep(1)
sour_page = driver.page_source
soup = BeautifulSoup(sour_page,'lxml')
img = str(soup.select('#TANGRAM__PSP_10__verifyCodeImg')[0]).split('=')[3].split('"')[1]
# print(img)
html = requests.get(img)
with open('picture.png', 'wb') as file:
    file.write(html.content)

write = input('输入验证码：')
driver.find_element_by_css_selector('#TANGRAM__PSP_10__verifyCode').send_keys(write)
driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit').click()
driver.implicitly_wait(8)
if myuser == driver.find_element_by_css_selector('#s_username_top > span').text:
    print('登陆成功')
driver.get_screenshot_as_file('baidu.png')
driver.quit()

