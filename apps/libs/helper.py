#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-26 23:37
# File    : helper.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

def is_isbn_or_key(word):
    """
    以下代码是用来判断q是isbn还是关键字；
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
