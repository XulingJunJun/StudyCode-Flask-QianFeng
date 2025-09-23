# views.py 路由 + 视图函数

# from App import

from flask import Blueprint, render_template

# 两种蓝图
blue = Blueprint('user', __name__)
product = Blueprint('product', __name__)
@blue.route('/')
@blue.route('/index')
# @app.route('/')
def index():
    zhangsan = {
        'name': 'ZhangSan',
        'age': 18,
        'hobby': ['football', 'swimming']
    }
    # 解包
    # return render_template('index.html',**zhangsan)
    # return render_template('index.html',name='张三', age=18, hobby=['football', 'swimming'])

    # block标签
    # return render_template('base.html')
    # return render_template('child1.html')
    return render_template('child2.html', **zhangsan)
@product.route('/product')
# from .views import *时,蓝图和函数不能同名
def pro():
    return 'product'

# -------------------------------------------------------------------------------------------------------------------------------------------------------

