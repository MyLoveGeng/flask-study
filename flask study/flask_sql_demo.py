from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:321708..@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 动态跟踪数据库修改，未来版本会移除
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello flask"

if __name__ == "__main__":
    app.run(debug=True)