#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-28 09:04
# File    : test3.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from werkzeug.local import LocalStack
s = LocalStack()
s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
