#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 08:44
# File    : book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import jsonify, request

from apps.libs.helper import is_isbn_or_key
from apps.spider.yushu_book import YushuBook
from apps.web import web
from apps.forms.book import SearchForm
from apps.view_models.book import BookViewModel
from apps.view_models.book import BookCollection


@web.route('/book/search')
def search():
    """
        q：普通关键字，ISBN；
        page：ModuleNotFoundError: No module named 'urllib2'
        ?q = 金庸&
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()  # q=9787501524044
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YushuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_isbn(q, page)
        books.fill(yushu_book, q)
        return jsonify(books)
    else:
        return jsonify(form.errors)
