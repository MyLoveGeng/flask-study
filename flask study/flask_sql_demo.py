from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:321708..@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 动态跟踪数据库修改，未来版本会移除
db = SQLAlchemy(app)


class Roles(db.Model):
    # 定义表名
    __tablename__ = 'Roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    role_id = db.Column(db.Integer, db.ForeignKey("Roles.id"))

@app.route('/')
def index():
    return "Hello flask"

if __name__ == "__main__":
    # 删除表
    db.drop_all()

    # 创建表
    db.create_all()

    app.run(debug=True)