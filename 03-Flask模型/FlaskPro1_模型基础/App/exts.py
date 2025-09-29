# exts.py 插件管理

#1.导入第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 2.初始化
# ORM(类-->模型)
sqlalchemy = SQLAlchemy()

# 数据库迁移(模型-->表)
migrate = Migrate()

# 3.声明和app对象绑定函数
def init_exts(app):
    sqlalchemy.init_app(app=app)
    migrate.init_app(app=app, db=sqlalchemy)