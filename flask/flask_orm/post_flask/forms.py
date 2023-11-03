from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm, fields


class PostForm(FlaskForm):
    id = fields.IntegerField(validators=[DataRequired()])


























