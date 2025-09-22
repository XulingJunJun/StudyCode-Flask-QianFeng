# views.py 路由 + 视图函数
# 删除错误的导入，并添加正确的导入
import datetime

from flask import Blueprint, render_template, request, session, make_response, redirect

# 两种蓝图
blue = Blueprint('user', __name__)
product = Blueprint('product', __name__)


@product.route('/product')
# from .views import *时,蓝图和函数不能同名
def pro():
    return 'product'


# -------------------------------------------------------------------------------------------------------------------------------------------------------

@blue.route('/')
@blue.route('/index/')
def index_method():
    # 从session中获取用户名
    username = session.get('user')
    return render_template('index.html', username=username)


@blue.route('/login/', methods=['GET', 'POST'])
def login_method():
    # 访问登录页面
    # 不是 else if ，而是 elif
    if request.method == 'GET':
        return render_template('login.html')
    # 点击登录按钮
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if username == 'lisi' and password == '123':
            # 将用户名和密码保存在session中(cookies中不能有中文)
            session['user'] = username
            #
            session.permanent = True

            response = redirect('/index')

            # 设置session的过期时间
            response.set_cookie('user', username, max_age=3600 * 24 * 7)
            # response.set_cookie('user', username, expires=datetime.datetime(2025, 12, 12))

            # 登录成功后，跳转到首页
            return response
        else:
            return render_template('login.html', error='用户名或密码错误')
    return None


@blue.route('/logout/')
def logout_method():
    # 删除session中的数据
    session.pop('user')
    # 删除cookies中的数据
    response = redirect('/index')
    response.delete_cookie('user')
    return response
