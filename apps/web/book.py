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


@web.route('/book/search')
def search():
    """
        q：普通关键字，ISBN；
        page：ModuleNotFoundError: No module named 'urllib2'
        ?q = 金庸&
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()  # q=9787501524044
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YushuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        # return jsonify({'msg':'参数校验失败！'})
        return jsonify(form.errors)
