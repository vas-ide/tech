
from datetime import datetime
from flask import Flask, request

from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators


class ContactForm(FlaskForm):
    current_daytime = datetime.now()

    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35),
        validators.Optional(),
        validators.AnyOf(values=["IT", "HR", "ATC"]),
        validators.InputRequired()
    ])
    birthday = DateField(label='Birthday', validators=[
        validators.DataRequired(current_daytime.month)
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
