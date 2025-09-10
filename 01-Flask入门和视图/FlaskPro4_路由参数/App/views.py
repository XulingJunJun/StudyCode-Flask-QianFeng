# views.py 路由 + 视图函数
import uuid

# from App import

from flask import Blueprint

blue = Blueprint('user', __name__)
product = Blueprint('product', __name__)
@blue.route('/')
# @app.route('/')
def index():
    return 'index'

@product.route('/product')
# 蓝图和函数不能同名
def pro():
    return 'product'

#1. 带参数类型的语法：<converter:variable_name>，其中converter为参数类型，常见类型如下：
  # a. string：接收任何没有斜杠（'/'）的文件（默认）
  # b. int：接收整型
  # c. float：接收浮点型
  # d. path：接收路径，可接收斜线（'/'）
  # e. uuid：只接受uuid字符串（唯一码，一种生成规则）
  # f. any：可以同时指定多种路径，进行限定


# 1.String
# @blue.route('/string/<string:username>/')
@blue.route('/string/<username>/')
def get_string(username):
    print(type(username))
    return 'string: %s' % username


# 2.Int :接收整型,传浮点报错
@blue.route('/int/<int:id>/')
def get_int(id):
    print(type(id))
    # TypeError: The view function did not return a valid response. The return type must be a string, dict, list, tuple with headers or status, Response instance, or WSGI callable, but it was a int.
    # string, dict, list, tuple
    # return str(id)
    return 'id: %s' % id

# 3.Float : 接收浮点型,传整型报错
@blue.route('/float/<float:money>/')
def get_float(money):
    print(type(money))
    return 'float: %s' % money

# 4.Path : 接收路径，可接收斜线（'/'）
@blue.route('/path/<path:name>/')
def get_path(name):
    print(type(name))
    return 'path: %s' % name

# 5.UUID : 只接受uuid字符串（唯一码，一种生成规则）
@blue.route('/uuid/<uuid:id>/')
def get_uuid(id):
    print(type(id))
    return 'uuid: %s' % id

# 生成uid :e71756f6-8dfc-11f0-ae75-7008942953be
@blue.route('/product_uuid/')
def product_uuid():
    import uuid
    return str(uuid.uuid1())

# 6.any:只能从所给元组中传值
@blue.route('/any/<any(male,female):gender>')
def get_any(gender):
    print(type(gender))
    return str(gender)


# method 请求方式

@blue.route('/method/')
# @blue.route('/method/', methods=['GET', 'POST'])
def get_method():
    return 'method'

