from flask import Flask, render_template

app = Flask(__name__)


# 如何返回一个网页（模板）
# 如何给模板填充数据
@app.route('/')
def index():
    # 传入数据
    url_str = 'http://www.eappo.site'
    # 显示模板
    my_list = [1, 2, 3, 4, 5, 6]
    my_dict = {
        'name': 'eappo',
        'age': 20
    }
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict)


if __name__ == '__main__':
    # 启动服务器
    app.run(debug=True)
