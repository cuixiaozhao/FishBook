#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FishBook 
# Software: PyCharm
# Time    : 2018-09-25 23:54
# File    : fisher.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask

# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/hello/', methods=['GET', 'POST'])  # 此种装饰器注册路由的方式，优雅但是不够灵活！
def hello():
    # 1/0
    # 基于类的视图(即插视图)
    return "Hello World！Base WebFramework Flask"


# 不优雅但是足够灵活的路由注册方式,最好使用"装饰器"，但是 基于类的视图(即插视图)，必须使用如下这种基于add_url_rule，不过两种理由的本质都是add_url_rule；
# app.add_url_rule('/hello/', view_func=hello)

if __name__ == '__main__':  # 约定俗成的用法，入口文件中，如果没有的话，fisher的文件会执行！添加上的话，保证生产环境不会执行！
    # 生产环境部署的方式：nginx + uWSGI；
    # app.run(host = '192.168.0.101',debug=True)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
    # 调试模式不能暴露到生产环境，debug=False，且debug模式性能比较差！
    # 无论是开发、测试还是生产，尽可能保证源代码的"镜像关系"性质！引出配置文件；

"""
小结：if __name__ == "__main__"的作用：
1、生产环境一般都是nginx + uwsgi的部署模式，不会使用flask内置的web服务器；
2、加上一句判断，一个Python源码文件（.py）除了可以被直接运行外，还可以作为模块（也就是库），
被其他.py文件导入。不管是直接运行还是被导入，
.py文件的最顶层代码都会被运行（Python用缩进来区分代码层次），
而当一个.py文件作为模块被导入时，我们可能不希望一部分代码被运行。
"""
