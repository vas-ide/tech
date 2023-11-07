
from datetime import datetime

from posts_upd.database import db


class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(50), default='unknown')
    review = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return 'GuessBookItem %r' % self.id

    def __str__(self):
        return f"Author-{self.author_name:>50}     ---    {self.review}"


# >>> from app import app, db, GuessBookItem
# >>> app.app_context().push()
# >>> db.create_all()
# >>> one = GuessBookItem(author_name='VAS', review='AQUAVITA The best!')
# >>> two = GuessBookItem(author_name='vas', review='IZUMRUD cool place')
# >>> three = GuessBookItem(author_name='Rostov-Community',review='GreenvichPark popular spa in Rostov Area')
# >>> db.session.add(one)
# >>> db.session.add(two)
# >>> db.session.add(three)
# >>> db.session.commit()