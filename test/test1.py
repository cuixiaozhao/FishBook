#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 22:44
# File    : test1.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, current_app

app = Flask(__name__)
# a = current_app
# d = current_app.config['DEBUG']

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']



# 文件的读写操作；
f = open(r"")

