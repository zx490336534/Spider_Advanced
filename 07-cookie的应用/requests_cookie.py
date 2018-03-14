import requests
import json

from requests.cookies import RequestsCookieJar

s = requests.session()
s.verify = False
s.get('https://weibo.cn/')
jar = RequestsCookieJar()
file = 'sina_cookies.txt'
with open(file,'r') as f:
    cookies = json.load(f)
    for cookie in cookies:
        # jar.set(cookie['name'],cookie['value'],path=cookie['path'],domain=cookie['domain'])
        jar.set(cookie.pop('name'),cookie.pop('value'))


url = 'https://weibo.cn/?tf=5_009'
r = s.get(url,cookies = jar)
r.encoding = 'UTF-8'
print(r.text)
