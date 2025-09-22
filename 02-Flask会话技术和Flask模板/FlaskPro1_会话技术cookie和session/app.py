# 1.__init__.py :初始文件,创建Flask应用
# import flask
# from flask import Flask
#
# 2.app = flask.Flask(__name__)
# views.py 路由 + 视图函数
# @app.route('/')
# def index():
#     return 'Hello World!'
from datetime import timedelta

from App import create_app

app = create_app()

if __name__ == '__main__':
    print(app.config)

    # 设置密钥
    app.config['SECRET_KEY'] = '123456'
    # 设置session的过期时间
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    app.run(debug=True)
