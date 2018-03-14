import gevent
import requests
import json
import time
import sys
sys.setrecursionlimit(100000)
offset = 0
url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

def DouyuSpider(offset):

    item = {}
    content = requests.get(url=url+str(offset),headers=headers).content.decode()
    data_list = json.loads(content)['data']
    if not data_list:
        return
    for data in data_list:
        item['room_id'] = data['room_id']
        item['anchor_city'] = data['anchor_city']
        item['vertical_src'] = data['vertical_src']
        item['nickname'] = data['nickname']
        write_img(item)
    time.sleep(1)

def write_img(item):
    print('正在存储来自%s的%s,他的房间地址是：https://www.douyu.com/%s' % (item['anchor_city'],item['nickname'],item['room_id']))
    content = requests.get(url=item['vertical_src'],headers=headers).content
    with open(''
              'img/'+item['nickname']+'.jpg','wb') as f:
        f.write(content)

if __name__ == '__main__':
    for i in range(1,1000,20):
        DouyuSpider(i)
