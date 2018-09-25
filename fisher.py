#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-25 23:54
# File    : fisher.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask

app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    # 基于类的视图(即插视图)
    return "Hello World！Base WebFramework Flask"


if __name__ == '__main__':
    app.run()
