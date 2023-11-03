from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired, length
from wtforms_alchemy import ModelForm, fields


class PostForm(FlaskForm):
    id = IntegerField(label='ID', validators=[DataRequired()])
    review = TextAreaField(label='Review', validators=[DataRequired(), length(5, 2500)])
