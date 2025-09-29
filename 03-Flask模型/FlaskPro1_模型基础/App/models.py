# models.py 模型数据库

from .exts import sqlalchemy

# 必须继承sqlalchemy.Model才能和数据库结构关联.
class User(sqlalchemy.Model):
    # 表名
    __tablename__ = 'tb_user'

    # 字段名
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(30), unique=True, index=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    sex = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    salary = sqlalchemy.Column(sqlalchemy.Float, default=100000, nullable=False)
    salary2 = sqlalchemy.Column(sqlalchemy.Float, default=100000, nullable=False)


# 模型-->数据库
# 类-->表结构
# 类属性-->表字段
# 一个对象-->表的一行数据

# db.Column : 表示字段
# db.Integer：表示整数
# primary_key=True ： 主键
# autoincrement=True ： 自动递增
# db.String(30): varchar(30) 可变字符串
# unique=True : 唯一约束
# index=True : 普通索引
# default=1 ： 默认值
# nullable=False : 是否允许为空