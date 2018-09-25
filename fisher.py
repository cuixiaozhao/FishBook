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


# @app.route('/hello/', methods=['GET', 'POST'])# 此种装饰器注册路由的方式，优雅但是不够灵活！
def hello():
    # 1/0
    # 基于类的视图(即插视图)
    return "Hello World！Base WebFramework Flask"


# 不优雅但是足够灵活的路由注册方式,最好使用"装饰器"，但是 基于类的视图(即插视图)，必须使用如下这种基于add_url_rule，不过两种理由的本质都是add_url_rule；
app.add_url_rule('/hello/', view_func=hello)

if __name__ == '__main__':
    app.run(debug=True)
