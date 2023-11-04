from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from tech.flask.flask_orm.post_flask import config
from tech.flask.flask_orm.post_flask.forms import PostForm
from tech.flask.flask_orm.post_flask.models import GuessBookItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# db.init_app(app)
db.create_all()
# app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def index():


    form = PostForm(request.form)

    post = GuessBookItem(**form.data)
    db.session.add(post)
    db.session.commit()
    posts = GuessBookItem.query.all()
    tes_lst = [datetime.now(), datetime.utcnow()]

    return render_template('index.html',
                           # form=posts
                           # form=tes_lst
                           )




def populate_db():
    vas = GuessBookItem(author_name='VAS', review='AQAVITA один изу лучших спа курортов на горячих источниках в поселке Мостовском Краснодарского Края.')
    db.session.add(vas)
    db.session.commit()  # note



@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html')


if __name__ == '__main__':
    from models import *

    # if PostForm.query.count() == 0:
    #     populate_db()

    app.run()
