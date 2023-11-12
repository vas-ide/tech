import traceback
from datetime import datetime

from flask import Flask, render_template, request, redirect

from posts_upd import app
from posts_upd.database import db
from posts_upd.forms import ReviewForm, AnswerForm
from posts_upd.models import Review, User, Answer


@app.route('/')
def index():
    posts = Review.query.order_by().where(Review.active == 1).all()
    users = User.query.all()
    current_date = datetime.now().date()
    time_Mos = f"MOS - {datetime.now().time()}"[0:-7]
    time_UTC = f"UTC - {datetime.utcnow().time()}"[0:-7]
    time_lst = [current_date, time_UTC, time_Mos]

    return render_template('index.html',
                           time_lst=time_lst,
                           posts=posts,
                           users=users,
                           )


@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def posts_detail(id):
    print(request.form)
    author = User.query.get(Review.query.get(id).user_id)
    post = Review.query.get(id)
    answers = Answer.query.where(Answer.review_id == id).all()
    if request.method == "POST":
        writer = request.form['writer']
        if len(writer) < 1:
            writer = "Anonymous"
        answer = request.form['answer']
        answer_obj = Answer(review_id=id, writer=writer, answer=answer)
        form = AnswerForm(request.form)
        if form.validate():
            try:
                db.session.add(answer_obj)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return f"Error - {e} \n {traceback.print_exc()}"
        else:
            return render_template('post_detail.html', author=author, post=post, answers=answers)
    else:
        return render_template('post_detail.html', author=author, post=post, answers=answers)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        author = request.form['author']
        if len(author) >= 1:
            for item in User.query.all():
                if item.username == author:
                    user_obj = User.query.where(User.username == author).first()
        else:
            user_obj = User.query.where(User.id == 1).first()
        title = request.form['title']
        review = request.form['review']
        if len(title) < 1:
            add_review = Review(user=user_obj, review=review)
        else:
            add_review = Review(user=user_obj, title=title, review=review)
        form = ReviewForm(request.form)
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
