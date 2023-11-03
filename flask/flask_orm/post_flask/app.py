



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tech.flask.flask_orm.post_flask import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
app.app_context().push()

@app.route('/')
def index():
    pass

@app.route('/create', methods=['POST'])
def create():
    pass

























