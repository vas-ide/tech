import traceback
from datetime import datetime

from flask import Flask, render_template, request, redirect

from posts_upd import app
from posts_upd.database import db
from posts_upd.forms import PostForm
from posts_upd.models import GuessBookItem


@app.route('/')
def index():
    posts = GuessBookItem.query.order_by(GuessBookItem.author_name.desc()).where(GuessBookItem.active == 1).all()
    current_date = datetime.now().date()
    time_Mos = f"MOS - {datetime.now().time()}"[0:-7]
    time_UTC = f"UTC - {datetime.utcnow().time()}"[0:-7]
    time_lst = [current_date, time_UTC, time_Mos]

    return render_template('index.html',
                           time_lst=time_lst,
                           posts=posts
                           )


@app.route('/posts/<int:id>')
def posts_detail(id):
    post = GuessBookItem.query.get(id)
    return render_template('post_detail.html', post=post)


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
