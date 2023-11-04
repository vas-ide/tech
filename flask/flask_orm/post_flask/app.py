from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


from tech.flask.flask_orm.post_flask import config
from tech.flask.flask_orm.post_flask.models import GuessBookItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def index():
    from tech.flask.flask_orm.post_flask.models import GuessBookItem
    from tech.flask.flask_orm.post_flask.forms import PostForm

    # form = PostForm(request.form)
    #
    # post = GuessBookItem(**form.data)
    # db.session.add(post)
    # db.session.commit()

    # posts = GuessBookItem.query.all()
    tes_lst = [datetime.now(), datetime.utcnow()]

    return render_template('index.html',
                           # form=posts
                           form=tes_lst
                           )


@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run()
