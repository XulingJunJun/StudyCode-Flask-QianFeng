# views.py 路由 + 视图函数

# from App import

from flask import Blueprint, request, render_template, jsonify, make_response ,Response

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


# 1.测试request参数
@blue.route('/request/' , methods=['GET','POST'])
def get_request():
    # 1.1
    print(request)


    print(request.method)

    print('------------------------------------------------------------------')

    # 1.2 get 参数
    print(request.args) #ImmutableMultiDict
    # print(request.args['name'] ,'defaulName') #没有参数会报错
    print(request.args.get('name')) #推荐使用
    print(request.args.getlist('name'))

    print('------------------------------------------------------------------')

    # 1.3 post参数
    print(request.form)
    # 与get参数一样的数据类型:ImmutableMultiDict
    # print(request.args['name'] ,'defaulName') #没有参数会报错
    print(request.form.get('name')) #推荐使用
    print(request.form.getlist('name'))

    print('------------------------------------------------------------------')

    # 1.4 cookie参数 (获取时不用使用args或者from)
    # cookies 的值必须是字符串类型。
    #在 cookies 中使用了中文字符 '王五'，但 HTTP headers 需要使用 latin-1 编码，无法直接处理中文字符。
    print(request.cookies)

    print('------------------------------------------------------------------')

    # 1.5 路径参数
    print(request.path)
    print(request.url)
    print(request.base_url)
    print(request.host_url)
    print(request.remote_addr)
    print('------------------------------------------------------------------')

    # 6.其他参数
    print(request.files)
    print(request.headers)
    print(request.user_agent)

    return 'request ok'


# 2.测试response参数
@blue.route('/response/')
def get_response():
    pass

    # 1.响应字符串
    # return 'response OK!'

    # 2.响应模板渲染
    # return render_template('index.html', name='张三', age=33)

    # 3.响应json对象(字典)
    data = {'name': '张三', 'age': 33}
    # return data
    # 响应json字符串
    # return jsonify(data)


    # 4.响应自定义对象
    html = render_template('index.html', name='张三', age=33)
    print(html, type(html))
    # 两种响应方式
    res = make_response(html, 200)
    res = Response(html,300)
    return res


