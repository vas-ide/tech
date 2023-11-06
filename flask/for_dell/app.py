import traceback
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from tech.flask_orm_posts import config
from tech.flask.flask_orm_posts.models import GuessBookItem

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# app.app_context().push()



@app.route('/')
def index():
    from tech.flask.flask_orm_posts.models import GuessBookItem
    posts = GuessBookItem.query.all()
    time_lst = [datetime.now(), datetime.utcnow()]

    return render_template('index.html',
                           date=time_lst,
                           # posts=posts
                           )


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html')
    if request.method == "POST":
        author_name = request.form['author']
        review = request.form['review']
        add_review = GuessBookItem(author_name=author_name, review=review)
        try:
            db.session.add(add_review)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error - {e} \n {traceback.print_exc()}"


if __name__ == '__main__':
    app.run(host='LocalHost', port='5500')
