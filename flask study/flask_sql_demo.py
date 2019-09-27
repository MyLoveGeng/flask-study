from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_, not_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:321708..@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 动态跟踪数据库修改，未来版本会移除
db = SQLAlchemy(app)


class Role(db.Model):
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

    def __str__(self):
        return "<{} {} {}>" .format (self.id, self.name, self.role_id)



@app.route('/add')
def add():
    role = Role(name='admin')
    user1 = User(id = 1, name='eappo', role_id=1)
    user2 = User(id = 2, name='eappo', role_id=1)
    user3 = User(id = 3, name='eappo', role_id=1)
    db.session.add(role)
    db.session.add_all([user1, user2, user3])
    db.session.commit()
    return "Hello flask"

@app.route('/update')
def update():
    user = User.query.get(1)
    user.name = 'geng'
    db.session.commit()
    return "hello update"

@app.route('/remove')
def remove():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return "hello remove"

@app.route('/select')
def select():
    # 可以用sqlalchemy中的方法去查询（利用数据查询对象 query）
    # a = db.session.query(User.id).all()
    # a = db.session.query(User.id).first()
    # a = db.session.query(User.id).all()[1:2]
    ## order_by
    # a = db.session.query(User.id).order_by(User.id)
    # a = db.session.query(User.id).order_by(-User.id)
    # for x in a:
    #     print(x)
    # fiter筛选器
    # a = User.query.filter(User.id==1).first()
    # a = User.query.filter(User.name.like('%e%'))
    # a = User.query.filter(User.id.in_((2, 3)))
    # a = User.query.filter(~User.id.in_((2, 3)))
    # a = db.session.query(User).filter(User.name.is_(None))
    # a = db.session.query(User).filter(User.name.isnot(None))
    # for x in a:
    #     print(x.name)
    ## 与或非
    # a = User.query.filter(and_(User.name == 'eappo', User.id == 1)).count()  # 与
    # a = User.query.filter(or_(User.name == 'eappo', User.id == 1)).count()  # 或
    # a = User.query.filter(not_(User.id == 1)).count()  # 非
    # print(a)
    #

    # 增加和删除的话都是需要提交才可以的
    # a = db.session.execute("select * from users")
    return "Select"

if __name__ == "__main__":
    # 删除表
    # db.drop_all()

    # 创建表
    # db.create_all()

    app.run(debug=True)