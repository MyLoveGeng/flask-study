# 导入扩展
from flask import Flask
# 创建flask应用程序实例
# # 确定资源所在路径
app = Flask(__name__)

# 定义路由及视图函数
# # flask中定义路由是通过装饰器实现
# # 路由默认只支持GET，如果需要增加，需要自行指定
@app.route('/')
def hello_world():
    return 'https://dormousehole.readthedocs.io/en/latest/quickstart.html'

@app.route('/geng')
def eappo():
    return 'geng'

# # <>定义路由参数, <>内需要起名字
@app.route('/user/<username>')
def show_user_profile(username):  # 需要填入视图名
    # 访问： http://0.0.0.0:5000/user/geng
    return username

@app.route('/user/<int:order_id>')
def show_int_id(order_id):
    return str(order_id)  # 类型是int时，返回值一定是字符串



if __name__ == '__main__':
    # 启动服务器
    app.run()
