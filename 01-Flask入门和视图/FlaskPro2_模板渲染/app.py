from tkinter.font import names

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!11'


if __name__ == '__main__':
    app.run(debug=True)

    # run()
    # 启动的时候还可以添加参数:
    # debug是否开启调试模式, 开启后修改过python代码会自动重启
    # port启动指定服务器的端口号, 默认是5000
    # host 主机, 默认是127.0.0.1 指定为0.0.0.0代表本机所有ip