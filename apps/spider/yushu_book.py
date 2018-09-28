#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 07:25
# File    : yushu_book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from apps.libs.httper import HTTP
from flask import current_app


class YushuBook:
    # 模型层；MVC,M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword_url = 'http:/t.yushu.im/v2/book/search?q={}&count={}&start={}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&page={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # book = query_from_mysql(isbn)
        # if book:
        #     return book
        # else:
        #     save(result)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
