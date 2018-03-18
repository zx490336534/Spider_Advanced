#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-14 21:44:04
# Project: v2ex_project

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.v2ex.com/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        # 取得本页面中 所有 a标签，属性 href 以  https://www.v2ex.com/?tab= 开头的 标签对象
        # response.doc 是应用的 pyquery的语法
        for link_a in response.doc('a[href^="https://www.v2ex.com/?tab="]').items():
            self.crawl(link_a.attr.href, callback=self.tab_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def tab_page(self, response):
        for link_a in response.doc('a[href^="https://www.v2ex.com/go/"]').items():
            self.crawl(link_a.attr.href, callback=self.go_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def go_page(self, response):
        # 爬取当前页面的所有帖子
        for link_a in response.doc('a[href^="https://www.v2ex.com/t/"]').items():
            self.crawl(link_a.attr.href, callback=self.detail_page, validate_cert=False)

        # 翻页，获取所有页的内容
        for link_a in response.doc('a.page_normal').items():
            # 递归 爬取所有的页面，必须设置 age， 不然会无限死循环
            self.crawl(link_a.attr.href, callback=self.go_page, validate_cert=False)

        '''
         伪代码，也可以这样实现抓取所有页面
         1、获取到最大的 页码 max_pag
         2、  for i in range(2, max_pag+1):
                url = 'https://www.v2ex.com/go/qna?p=' + str(i)
                self.crawl(url, callback=self.go_page, validate_cert=False)
     '''

    @config(priority=2)
    def detail_page(self, response):
        result = {
            "url": response.url,
            "title": response.doc('title').text(),
        }
        return result

    # 用于接收这个 上面 的 return
    # result  就是 detail_page  返回的值
    def on_result(self, result):
        sql = 'insert into v2ex(url, title) values(%s, %s )'
        insert(sql, (result['url'], result['title']))


import pymysql

'''
    这个MySQL封装类，是没有实现连接池的，大家在项目的实际应用中。
    需要使用连接池，使用pymysqlpool或者自己实现一个连接池
'''

"""
db_config是一些数据库的配置文件
"""
class Mysql(object):
    def __init__(self):
        #数据库构造函数，从连接池中取出连接，并生成操作游标
        self._conn = Mysql.__getConn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn():
        """
        @summary : 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'v2ex',
            'charset': 'utf8'
        }
        config['cursorclass'] = pymysql.cursors.DictCursor
        conn = pymysql.connect(**config)
        return conn

    def getAll(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result
        list(字典对象) / boolean
        查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count>0:
            result = self._cursor.fetchall()
        else:
            result = []
        return result

    def getOne(self,sql,param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]
        传递进来
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result
        list / boolean
        查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count>0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self,sql,num,param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result  list / boolean  查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count>0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertOne(self,sql,value):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的ＳＱＬ格式
        @param value:要插入的记录数据tuple / list
        @return: insertId 受影响的行数
        """
        self._cursor.execute(sql, value)
        return self.__getInsertId()

    def insertMany(self,sql,values):
        """
        @summary: 向数据表插入多条记录
        @paramsql:要插入的ＳＱＬ格式
        @paramvalues:要插入的记录数据tuple(tuple) / list[list]
        @return: count受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id, 如果没有则为０
        """
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']

    def __query(self,sql,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count

    def update(self,sql,param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用( % s, % s)
        @param param: 要更新的值  tuple / list
        @return: count 受影响的行数
        """
        return self.__query(sql,param)

    def delete(self,sql,param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用( % s, % s)
        @param param: 要删除的条件  值  tuple / list
        @return: count受影响的行数
        """
        return self.__query(sql,param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self,option='commit'):
        """
        @summary: 结束事务
        """
        if option=='commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd==1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()


def insert(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.insertOne(sql, params)
    finally:
        mysql.dispose()
    return ret

def insert_many(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.insertMany(sql, params)
    finally:
        mysql.dispose()
    return ret

def delete(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.delete(sql, params)
    finally:
        mysql.dispose()
    return ret

def update(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.update(sql, params)
    finally:
        mysql.dispose()
    return ret

def get_one(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.getOne(sql, params)
    finally:
        mysql.dispose()
    return ret

def get_many(sql, params=None, num=None):
    mysql = Mysql()
    try:
        ret = mysql.getMany(sql, num, params)
    finally:
        mysql.dispose()
    return ret

def get_all(sql, params=None):
    mysql = Mysql()
    try:
        ret = mysql.getAll(sql, params)
    finally:
        mysql.dispose()
    return ret

