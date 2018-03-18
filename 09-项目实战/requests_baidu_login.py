import random

import math
import requests
import time


def gid_encrypt():
    s_raw = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'

    s_ret = ''
    for s in s_raw:
        t = random.randint(0, 16)
        if 'x' == s:
            n = t
            s_ret += hex(n)[-1:]
        elif 'y' == s:
            n =  3 & t | 8
            s_ret += hex(n)[-1:]
        else:
            s_ret += s

    return s_ret.upper()


class BaiDu(object):

    DEAFULT_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

    def __init__(self):
        self.s = requests.session()
        self.s.verify = False
        self.s.headers = self.DEAFULT_HEADERS


    def start(self):
        self.visit_index()

    def visit_index(self):
        url = 'https://www.baidu.com'
        self.s.get(url)

    def visit_api(self):
        url = 'https://passport.baidu.com/v2/api/'
        self.gid = gid_encrypt()
        params = {
            'getapi':'',
            'tpl':'mn',
            'apiver':'v3',
            'tt':get_13_time(),
            'class':'login',
            'gid':self.gid,
            'loginversion':'v4',
            'logintype':'dialogLogin',
            'traceid':'',
            'callback':'bd__cbs__cp7c9g',
        }
        r = self.s.get(url,params=params)
        r.encoding = 'UTF-8'
        print(r.text)

    def get_call_back(self,e = 'bd__cbs__'):
        return e + to_string_private(math.floor(2147483648 * random.random()),36)

def get_13_time():
    return str(int(time.time()*1000))




if __name__ == '__main__':
