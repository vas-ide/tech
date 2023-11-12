from datetime import datetime

from posts_upd.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='user')

    def __repr__(self):
        return f"User-{self.username} id{self.id}"


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=1, index=True)
    title = db.Column(db.String(150), default='Daily')
    review = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)
    answers = db.relationship('Answer', backref='review')


    def __repr__(self):
        return f"Theme-{self.title}    Author-{self.user}    Review-{self.review}"


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False, index=True)
    writer = db.Column(db.String(50), default='Anonymous')
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.answer}"