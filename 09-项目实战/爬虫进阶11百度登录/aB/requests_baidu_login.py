#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import math
import re
from urllib.parse import urlencode

import io
import requests
import time
import urllib3
from PIL import Image

urllib3.disable_warnings()

__author__ = 'Terry'

def gid_encrypt():
    s_raw = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'

    s_ret = ''
    for s in s_raw:
        t = random.randint(0, 16)
        if 'x' == s:
            n = t
            s_ret += hex(n)[-1:]
        elif 'y' == s:
            n = 3 & t | 8
            s_ret += hex(n)[-1:]
        else:
            s_ret += s

    return s_ret.upper()

# 得到 13 位的时间戳
def get_13_time():
    return str(int(time.time()*1000))

def to_string_private(num, n):
    '''
        得到一个随机字符串，由0-9 a-z 组成， 首字母不为0

    :param num:  要转换的整数值
    :param n:   要转换的位数，必须小于等于 36
    :return:  转换后的值
    '''
    return ((num == 0) and "0") or (to_string_private(num // n, n).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % n])

def to_string_private_1(num, n):
    n_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    if num == 0 :
        return '0'
    else:
        x, y = divmod(num, n)
        return to_string_private_1(x, n).lstrip('0') + n_chars[y]

        # return to_string_private_1(num // n, n).lstrip('0') + n_chars[num % n]

def get_first_str_by_text_multi(p, text):
    l = re.findall(p, text, re.M|re.S)
    return l[0]

class BaiDu(object):

    DEFAULT_HEADERS = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Referer': 'https://www.baidu.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

        self.s = requests.session()
        self.s.verify = False
        self.s.headers = self.DEFAULT_HEADERS

        self.s.proxies = {'https': '127.0.0.1:8888'}

    def start(self):
        self.visit_index()
        time.sleep(.5)
        self.visit_api()
        time.sleep(.5)
        self.visit_checklogin()
        time.sleep(.5)
        self.visit_get_getpublickey()
        time.sleep(.5)
        self.visit_genimage()
        time.sleep(.5)
        self.visit_checkvcode()

    def visit_index(self):
        url = 'http://www.baidu.com'
        self.s.get(url)

    def visit_api(self):
        url = 'https://passport.baidu.com/v2/api/?getapi&'
        self.gid = gid_encrypt()
        params = {
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'class': 'login',
            'gid': self.gid,
            'loginversion': 'v4',
            'logintype': 'dialogLogin',
            'traceid': '',
            'callback': self.get_callback(),
        }
        url = url + urlencode(params)
        r  = self.s.get(url)
        r.encoding = 'UTF-8'
        text = r.text
        self.token = get_first_str_by_text_multi('"token".*?:.*?"(.*?)"', text)
        # self.token = get_first_str_by_text_multi('"token".*?"(.*?)"', text)
        print('得到token')

    def visit_checklogin(self):
        url = 'https://passport.baidu.com/v2/api/?logincheck&'
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'sub_source': 'leadsetpwd',
            'username': self.user ,
            'loginversion': 'v4',
            # 'dv': 'tk0.276407821845840561518268251909@tto0zyAgPRnmX6D6Z06WtAL~wD6~hvnFhvLTCgBL57GJ~34kDfn1WRngnTvkI~4kqRCot7E~5hFCwv6tADLgopL~w~PyC-FStcB8pfA1DZ4kngATpTA-pp4tEhFWM8D6~vL~hF6teXntwvMLA3PWZVOJ6RAkI-n8pgngMe7k6RnmX6D6Z06WtAL~wD6~hvnFhvLTCgBL57GJ~34k6pAF2RngnTvmpp4tEhFWM8D6~vL~hF6teXntwvMLA3PWZVOJ6RA1qZnmpgngMeho0atAkPT4k2yn-pZ7koR4kozA9pfAk2RngPX4koznkoRCot7E~5hFCwv6tADLgopL~wSOywfBL5CFsw9KJZmMszRngnTvk6pA8pXn1qRn1Wz78X6D6Z06WtAL~wD6~hvnFhvLThVPTATOT5W4kngATp_yrrB~rIOwUvKhIoin8p-4kGf-ozMsRp412TA1DpAgI-nFIfAFIfnk6ynF6X7k2y7k2~nFWp7D__iobK0EfP0nb4-wTMTPUGStYB06UGywc4-X~OSE3BS3UBJD_Fopn12p4mfZn-pXnk6~4kng7mpXngGy4kPy7mpXngGy4kop7FDRAknXwo0vrnmpg78pyn-py7mpTn8pZ78pXnknRnFqZ4kogA8pXAk6RnFDz4ko~n8pX7kGRn1G-4k2znHp-7k6RngqX4kn-A8pgn1PRngnf4kngAp__',
            'traceid': '',
            'callback': self.get_callback(),
        }

        url = url + urlencode(params)
        r = self.s.get(url)
        r.encoding = 'utf-8'
        text = r.text
        self.codeString = get_first_str_by_text_multi('"codeString".*?:.*?"(.*?)"', text)
        self.vcodetype = get_first_str_by_text_multi('"vcodetype".*?:.*?"(.*?)"', text)
        print('得到codeString和vcodetype')

    def visit_get_getpublickey(self):
        url = 'https://passport.baidu.com/v2/getpublickey'
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'gid': self.gid,
            'loginversion': 'v4',
            'traceid': '',
            'callback': self.get_callback(),
        }

        r = self.s.get(url, params=params)
        r.encoding = 'UTF-8'
        text = r.text
        self.pubkey = get_first_str_by_text_multi('''"pubkey".*?:.*?'(.*?)',''', text)
        self.key = get_first_str_by_text_multi('''"key".*?:.*?'(.*?)',''', text)
        print('得到pubkey和key')

    def visit_genimage(self):
        url = 'https://passport.baidu.com/cgi-bin/genimage?' + self.codeString
        r = self.s.get(url)
        f_img = io.BytesIO(r.content)
        im = Image.open(f_img)
        im.save('baidu_vcode.jpg')

    def visit_checkvcode(self):
        vcode = input('请输入验证码')
        url = 'https://passport.baidu.com/v2/?checkvcode&a=1&a=2&a=3&a=4&'
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'verifycode': vcode,
            'loginversion': 'v4',
            'codestring': self.codeString,
            'traceid': '',
            'callback': self.get_callback(),
        }
        url = url + urlencode(params)
        r = self.s.get(url)
        r.encoding = 'utf-8'
        text = r.text

    def get_callback(self, e='bd__cbs__'):
        # return e + Math.floor(2147483648 * Math.random()).toString(36)
        return e + to_string_private(math.floor(2147483648 * random.random()), 36)

if __name__ == '__main__':
    user = 'mumuloveshine'
    pwd = 'mumu2018'
    baidu = BaiDu(user, pwd)
    baidu.start()
    # print(baidu.get_callback())