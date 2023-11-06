from datetime import datetime

from tech.flask.flask_orm_posts.database import db


class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(80), nullable=False)
    review = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    # def __str__(self):
    #     return f" Review Author - {self.author_name} >>> {self.review}"


# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from models import GuessBookItem
# >>> one = GuessBookItem(author_name='VAS', review='AQUAVITA The best!')
# >>> two = GuessBookItem(author_name='vas', review='IZUMRUD cool place')
# >>> three = GuessBookItem(author_name='Rostov-Community',review='GreenvichPark popular spa in Rostov Area')
# >>> db.session.add(one)
# >>> db.session.add(two)
# >>> db.session.add(three)
# >>> db.session.commit()