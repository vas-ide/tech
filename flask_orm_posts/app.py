from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def index():


    # form = PostForm(request.form)
    #
    # post = GuessBookItem(**form.data)
    # db.session.add(post)
    # db.session.commit()
    # posts = GuessBookItem.query.all()
    # tes_lst = [datetime.now(), datetime.utcnow()]

    return render_template('index.html',
                           # form=posts
                           # form=tes_lst
                           )



@app.route('/create', methods=['GET', 'POST'])
def create():
    from models import GuessBookItem

    if request.method == "GET":
        return render_template('create.html')
    if request.method == "POST":
        author_name = request.form['author']
        review = request.form['review']
        add_review = GuessBookItem(author_name=author_name, review=review)
        try:
            db.session.add(add_review)
            db.session.commit()
            return redirect('create.html')
        except:
            return f"Some Error"


if __name__ == '__main__':
    app.run(host='LocalHost', port='5500')
