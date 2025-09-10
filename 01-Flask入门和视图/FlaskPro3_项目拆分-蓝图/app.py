# 1.__init__.py :初始文件,创建Flask应用
# import flask
# from flask import Flask
#
# 2.app = flask.Flask(__name__)
# views.py 路由 + 视图函数
# @app.route('/')
# def index():
#     return 'Hello World!'


from App import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)