

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ContactForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    password = StringField(label='JOB', validators=[
        validators.Length(min=6, max=35),
    ])
    password = StringField(label='JOB', validators=[
        validators.Length(min=6, max=35),
    ])

app = Flask(__name__)

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

@app.route('/form/user')
def e_password():
    pass
@app.route('/serve/<path:filename>')
def e_password():
    pass



if __name__ == "__main__":
    app.run()
