#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-27 09:17
# File    : __init__.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Blueprint

# 蓝图或者蓝本，blueprint；
web = Blueprint('web', __name__)

from apps.web import book
from apps.web import user
