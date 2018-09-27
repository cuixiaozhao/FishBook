#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 07:25
# File    : yushu_book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from httper import HTTP


class YushuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http:/t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
