import traceback
from datetime import datetime

from flask import Flask, render_template, request, redirect

from posts_upd import app
from posts_upd.database import db
from posts_upd.forms import PostForm
from posts_upd.models import GuessBookItem


@app.route('/')
def index():
    posts = GuessBookItem.query.all()
    time_lst = [datetime.now(), datetime.utcnow()]

    return render_template('index.html',
                           time_lst=time_lst,
                           posts=posts
                           )


@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == "POST":
        author_name = request.form['author']
        review = request.form['review']
        add_review = GuessBookItem(author_name=author_name, review=review)
        form = PostForm(request.form)
        if form.validate():
            try:
                db.session.add(add_review)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return f"Error - {e} \n {traceback.print_exc()}"
        else:
            return render_template('/create.html')
    else:
        return render_template('/create.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5555)
