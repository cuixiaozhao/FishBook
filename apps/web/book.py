#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 08:44
# File    : book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YushuBook
from apps.web import web
from apps.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
        q：普通关键字，ISBN；
        page：ModuleNotFoundError: No module named 'urllib2'
        ?q = 金庸&
    :return:
    """
    q = request.args['q']
    page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data.strip()
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
        else:
            result = YushuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg':'参数校验失败！'})