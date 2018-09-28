#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-28 09:04
# File    : test4.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from werkzeug.local import LocalStack
import threading
import time

my_stack = LocalStack()

my_stack.push(1)
print("In main thread after push,value is:" + str(my_stack.top))


def worker():
    print("In new thread before push,value is:" + str(my_stack.top))

    my_stack.push(2)
    print("In new thread before push,value is:" + str(my_stack.top))


new_t = threading.Thread(target=worker, name="cuixiaozhao_thread")
new_t.start()
time.sleep(1)
print("finally,in main thread value is:" + str(my_stack.top))
"""
In main thread after push,value is:1
In new thread before push,value is:None
In new thread before push,value is:2
finally,in main thread value is:1
"""
