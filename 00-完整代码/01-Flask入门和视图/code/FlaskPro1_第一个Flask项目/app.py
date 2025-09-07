# 导入Flask
from flask import Flask

# 创建Flask应用对象
app = Flask(__name__)


# 路由route + 视图函数hello_world
@app.route('/')
def hello_world():
    # 响应：返回给浏览器的数据
    return 'Hello World!'


# 添加一个路由和视图函数
@app.route('/index/')
def index():
    return 'Index 首页4'


if __name__ == '__main__':
    # 启动服务器
    app.run()
