#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-25 23:54
# File    : fisher.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=5000)
