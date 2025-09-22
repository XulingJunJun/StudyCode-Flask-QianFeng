# __init__.py :初始文件,创建Flask应用
import flask
from flask import Flask
from .views import *

# 创建Flask应用函数
def create_app():
        app = Flask(__name__)
        # 添加secret_key以启用session
        app.secret_key = 'your-secret-key-here'
        # 将蓝图注册到app中
        app.register_blueprint(blueprint=blue)
        app.register_blueprint(blueprint=product)
        return app

# app = flask.Flask(__name__)