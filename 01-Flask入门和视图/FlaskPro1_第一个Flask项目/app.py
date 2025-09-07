from flask import Flask

# Flask创建所在文件的的目录即为项目的根目录

# 创建Flask应用对象
app = Flask(__name__)


# 路由+视图函数
@app.route('/')
def hello_world():  # put application's code here
    # 响应:返回给浏览器数据
    return 'Hello World!'

@app.route('/index')
def index():
    return 'index 首页'


if __name__ == '__main__':
    # 运行Flask应用,启动服务器
    app.run()
