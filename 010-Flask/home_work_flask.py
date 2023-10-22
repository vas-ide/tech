import traceback

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo


class PassForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        DataRequired(),
        Email()
    ])
    password = PasswordField(label='Password', validators=[
        validators.Length(min=6, max=35),
        DataRequired()
    ])
    password_check = StringField(label='Repeat Password', validators=[
        validators.Length(min=6, max=35),
        DataRequired(),
        EqualTo('password')
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/locales')
def locales():
    data = "{'locales': ['ru', 'en', 'it']}"
    return data


@app.route('/sum/<int:first>/<int:second>/')
def sum(first, second):
    return f"sum={first + second}"


@app.route('/greet/<user_name>')
def greet(user_name):
    return f"Hello, {user_name}"


@app.route('/form/user', methods=['GET', 'POST'])
def e_password():
    if request.method == 'POST':
        print(request.form)
        form = PassForm(request.form)
        print(form.validate())
        errors_lst = []

        if form.validate():
            return f"{{'status': 0, 'errors': {errors_lst}}}"
        else:
            errors_lst.append(traceback.format_exc())
            return f"{{'status': 0, 'errors': {errors_lst}}}"

    if request.method == 'GET':
        return 'Hello unknown User', 200


@app.route('/serve/<path:filename>')
def path_dir():
    pass


if __name__ == "__main__":
    app.run()
