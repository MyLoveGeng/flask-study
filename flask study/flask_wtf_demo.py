from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'eappo'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username, password, password2]):
            flash("参数不完整")
        elif password != password2:
            flash("密码不一致")
        else:
            return 'success'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)