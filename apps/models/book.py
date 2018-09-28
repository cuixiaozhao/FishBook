#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 12:50
# File    : book.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
1、SQLAlchemy，WTForms；
2、Flask_SQLALchemy,基于SQLAlchemy的封装；
3、Flask_WTFORMS,基于WTForms的封装；
4、Flask的werkzeug也是第三方组件；
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
