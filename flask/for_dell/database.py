from flask_sqlalchemy import SQLAlchemy

from tech.flask_orm_posts.app import app

db = SQLAlchemy(app)