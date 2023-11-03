from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired, length
from wtforms_alchemy import ModelForm, fields

from tech.flask.flask_orm.post_flask.models import GuessBookItem
from tech.flask.flask_orm.sqlalchemy_example.models import Post


# class PostForm(FlaskForm):
#     id = IntegerField(label='ID', validators=[DataRequired()])
#     review = TextAreaField(label='Review', validators=[DataRequired(), length(5, 2500)])


class PostForm(ModelForm):
    class Meta:
        model = GuessBookItem
