# views.py 路由 + 视图函数

# from App import

from flask import Blueprint

# 两种蓝图
blue = Blueprint('user', __name__)
product = Blueprint('product', __name__)
@blue.route('/')
# @app.route('/')
def index():
    return 'index'

@product.route('/product')
# from .views import *时,蓝图和函数不能同名
def pro():
    return 'product'

# -------------------------------------------------------------------------------------------------------------------------------------------------------

