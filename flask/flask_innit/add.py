

import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    name_file = os.path.basename(__file__)
    lib_file = os.listdir("../010-Flask")
    doz = False
    if name_file in lib_file:
        doz = True
    return f"This is testing start app! Path-{__file__}, check-{doz}"


@app.route('/<int:part1>/<int:part2>/')
def parts_int(part1, part2):
    return f"This is  testing start app! a={part1} b={part2} sum={part1 + part2}"


@app.route('/<part1>/<part2>/<part3>/')
def parts_str(part1, part2, part3):
    result = max(len(part1), len(part2), len(part3))
    for i in [part1, part2, part3]:
        if len(i) == result:
            return f"This is  testing start app! Max-length={i}"



if __name__ == "__main__":
    app.run()
