import json
import random

import jsonpath
import requests

class DouBanSpider(object):
    def __init__(self):
        self.start = 0
        USER_AGENTS=["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",]
        self.headers = {'User-Agent':random.choice(USER_AGENTS)}

    def start_work(self):
        response = requests.get(url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start='+str(self.start) +'&limit=20')
        if response.text == '[]':
            print('end')
            return
        self.json_data(response.text)
        # try:
        #     self.json_data(response.text)
        # except:
        #     print('end')


    def json_data(self,data):
        data = json.loads(data)
        item = {}
        #电影名称
        title_list = jsonpath.jsonpath(data,'$..title')
        #电影类型
        types_list = jsonpath.jsonpath(data,'$..types')
        #电影评分
        score_list = jsonpath.jsonpath(data,'$..score')
        #电影url
        url_list = jsonpath.jsonpath(data,'$..url')
        #电影地区
        regions_list = jsonpath.jsonpath(data,'$..regions')

        for title,score,url,types,regions in zip(title_list,score_list,url_list,types_list,regions_list):
            item['title'] = title
            item['score'] = score
            item['url'] = url
            item['types'] = types
            item['regions'] = regions
            self.write_data(item)
            # print(item)
        print(self.start)
        self.start += 20

        self.start_work()

    def write_data(self,item):
        content = json.dumps(item,ensure_ascii=False) + ',\n'
        with open('Doubanmovie.json','a',encoding='utf-8') as f:
            f.write(content)




if __name__ == '__main__':
    work = DouBanSpider()
    work.start_work()