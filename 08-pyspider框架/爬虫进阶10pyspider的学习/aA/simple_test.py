#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-14 20:45:06
# Project: pyspider_test

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'GoogleBot',
        }
    }

    '''
        入口方法
    '''
    @every(minutes=12 * 60, seconds=10)
    def on_start(self):
        '''
            crawl，就相当于我们之前的那个  requests.get
        '''
        self.crawl('http://scrapy.org/', callback=self.index_page, validate_cert=False)

    '''
        虽然 pyspider 使用的 requests 库进行网络访问，
        但是这里的 response 并不是 requests库的get或post方法返回的response
        这里的response 是 pyspider 自己封装的一个类
    '''
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
