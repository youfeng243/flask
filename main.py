# encoding: utf-8
"""
@author: youfeng
@file: main.py
@time: 2018/11/16 下午10:39
"""
from flask.app import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "hello world!"


if __name__ == '__main__':
    application.run()
