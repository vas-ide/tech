






from datetime import datetime
from tech.flask.flask_orm.sqlalchemy_example.app import db



class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(80), nullable=True)
    review = db.Column(db.String(), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return f" Review Author - {self.author_name} >>> {self.review}"



