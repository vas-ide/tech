# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from tech.flask.flask_orm.sqlalchemy_example.models import User, Post


# class __PostForm(FlaskForm):  # This looks ugly!
#     user_id = fields.IntegerField(validators=[
#         validators.DataRequired(),
#     ])
#     title = fields.StringField(validators=[
#         validators.DataRequired(),
#     ])
#     content = fields.StringField(validators=[
#         validators.DataRequired(),
#     ])


# https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
class UserForm(ModelForm):
    class Meta:
        model = User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]
