#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 08:44
# File    : book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YushuBook
from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q：普通关键字，ISBN；
        page：ModuleNotFoundError: No module named 'urllib2'
    :return:
    """
    # ISBN13 :ISBN13,13个0~9的数字组成；
    # ISBN10 :10个0~9的数字组成,含有一些-；
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YushuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_keyword(q)
    return jsonify(result)
