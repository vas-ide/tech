import os
import traceback
from contextlib import contextmanager
from simple_settings import settings
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import random

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='some-secret-key',
    WTF_CRRF_ENABLED=False,
)
FLASK_RANDOM_SEED = 15
def next_number():
    random.seed(FLASK_RANDOM_SEED)
    while True:
        numb = random.randint(1, 1000)
        yield numb
numbers=next_number()
numb_lst = []
@app.route('/', methods=['GET'])
@app.route('/<int:number>', methods=['POST'])
def index_page(number=None):
    if request.method == 'GET':
        for numb in numbers:
            numb_lst.append(numb)
            return f"The number is hidden ! ---{numb}---"
    if request.method == 'POST':
        # if number == numb_lst[-1]:
        #     for numb in numbers:
        #         numb_lst.append(numb)
        if number == numb_lst[-1]:
            return f"Congratulations Numb was={numb_lst[-1]}"
        elif number > numb_lst[-1]:
            return f"Try again >>>  Numb{numb_lst[-1]}"
        elif number < numb_lst[-1]:
            return f"Try again <<<  Numb{numb_lst[-1]}"




if __name__ == '__main__':
    app.run()
