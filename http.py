#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-26 23:48
# File    : http.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
发送HTTP请求的方式：
1、urllib(难用)Useage:from urllib import request
2、requests(推荐使用)，pip install requests （注意尾部的s）
"""

import requests


class HTTP(object):
    # 经典类和新式类，Python2有区分，Python3统一为新式类；
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful API；
        # json格式的数据；
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ""


"""
简化代码if~else代码的几种方式：
1、三元表达式；
2、巧妙使用if~return的"特例"来简化代码书写，但是不建议一个函数有多个return，原则上一个函数只有一个return，return视为一个函数的终结；
3、将if~else提取成一个函数；
"""
