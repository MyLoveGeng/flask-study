from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = "eappo"

class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    password2 = PasswordField("确认密码", validators=[DataRequired(), EqualTo("password", "密码不一致")])
    submit = SubmitField("提交")

@app.route("/form", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if login_form.validate_on_submit():
            print(username, password, password2)
            return "success WTF"
        else:
            flash("error")
    return render_template("wtf_demo.html", login_form=login_form)

@app.route('/')
def hello_world():
    name = 'geng'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
