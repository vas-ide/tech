from app import app, db, Review, User

app.app_context().push()
db.create_all()
unknown = User(username='Unknown', email='unknown@known.com')
vas = User(username='VAS', email='vas.ide2022@gmail.com')
db.session.add(unknown)
db.session.add(vas)
db.session.commit()
one = Review(user=vas, title='SPA', review="AQUAVITA best SPA whits 5 pool's")
two = Review(user=vas, title='SPA', review="Izumrud cool place. SPA whits 3 pool's")
three = Review(user=vas, title='SPA', review="GreenvichPark popular SPA in Rostov Area")
db.session.add(one)
db.session.add(two)
db.session.add(three)
four = Review(review="Horse Rancho")
db.session.add(four)
db.session.commit()

