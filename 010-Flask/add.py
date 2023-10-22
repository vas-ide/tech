from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f"This is testing start app!"


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
