# __init__.py :初始文件,创建Flask应用
import flask
from flask import Flask
from .views import *
from .exts import *

# 创建Flask应用函数
def create_app():
        app = Flask(__name__)
        # 将蓝图注册到app中
        app.register_blueprint(blueprint=blue)
        app.register_blueprint(blueprint=product)

        #配置数据库
        db_uri = 'sqlite:///sqlite3.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改


        # 初始化插件
        init_exts(app=app)

        return app

# app = flask.Flask(__name__)