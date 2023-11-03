import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from tech.flask.flask_orm.post_flask import config
from tech.flask.flask_orm.post_flask.models import GuessBookItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# app.app_context().push()

@app.route('/')
def index():
    from tech.flask.flask_orm.post_flask.forms import PostForm

    # posts = GuessBookItem.query.all()
    tets_lst = [datetime.datetime.now()]

    return render_template('index.html',
                           # form=posts
                           form=tets_lst
                           )

@app.route('/create', methods=['POST'])
def create():
    pass


if __name__ == '__main__':



    app.run()
