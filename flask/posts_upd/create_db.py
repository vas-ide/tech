from app import app, db, GuessBookItem

app.app_context().push()
db.create_all()
one = GuessBookItem(author_name='VAS', review='AQUAVITA The best!')
two = GuessBookItem(author_name='vas', review='IZUMRUD cool place')
three = GuessBookItem(author_name='Rostov-Community', review='GreenvichPark popular spa in Rostov Area')
db.session.add(one)
db.session.add(two)
db.session.add(three)
db.session.commit()
