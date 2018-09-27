#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 09:18
# File    : __init__.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('apps.secure')
    app.config.from_object('apps.settings')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from apps.web.book import web
    app.register_blueprint(web)