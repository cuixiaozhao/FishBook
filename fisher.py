#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-25 23:54
# File    : fisher.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask, make_response

# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>', methods=['GET', 'POST'])
def search(q, page):
    """
        q：普通关键字，ISBN；
        page：
    :return:
    """
    # ISBN13 :ISBN13,13个0~9的数字组成；
    # ISBN10 :10个0~9的数字组成,含有一些-；


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=5000)
