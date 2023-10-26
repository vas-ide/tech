import os
from contextlib import contextmanager
from flask import Flask, request
from simple_settings import settings
import random

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='some-secret-key',
    WTF_CRRF_ENABLED=False,
)

FLASK_RANDOM_SEED = 15



list_of_nums = [1, 2, 3, 8, 15, 42]
def get_even(list_of_nums= [1, 2, 3, 8, 15, 42]) :
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
get_even()
# @app.route('/', methods=['GET', 'POST'])
# def index_page():
#     random.seed(FLASK_RANDOM_SEED)
#     number = None
#     for counter in range(10000):
#         if request.method == 'POST':
#             return
#         if request.method == 'GET':
#             number = random.randint(1, 100)
#             yield f"The number is hidden ! {number}", 200
#
#
# if __name__ == '__main__':
#     app.run()
