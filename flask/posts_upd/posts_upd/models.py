from datetime import datetime

from posts_upd.database import db


class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(50), default='unknown')
    review = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return f"Author-{self.author_name:>50}     ---    {self.review}"
