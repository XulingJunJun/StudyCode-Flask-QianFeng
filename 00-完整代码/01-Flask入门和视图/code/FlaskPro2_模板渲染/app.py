from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    # 返回字符串
    return 'Flask Home2'

# 模板渲染
@app.route('/index/')
def index():
    # 返回字符串: 支持HTML标签
    # return '<b>Flask Index</b>'

    # 模板渲染
    return render_template('index.html', name='法外狂徒张三')

    # JSON
    # jsonify: 序列化
    # return jsonify({'name': '张三', 'age': 33})



if __name__ == '__main__':
    # 启动
    app.run(debug=True)

    # app.run(debug=True, port=5000, host='0.0.0.0')
    # run()启动的时候还可以添加参数:
    #     debug 是否开启调试模式，开启后修改过python代码会自动重启
    #     port 启动指定服务器的端口号，默认是5000
    #     host 主机，默认是127.0.0.1，指定为0.0.0.0代表本机所有ip
