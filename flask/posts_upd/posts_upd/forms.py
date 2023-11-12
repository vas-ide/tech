from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, StringField, BooleanField, DateField
from wtforms.validators import DataRequired, length


from wtforms_alchemy import ModelForm
from posts_upd.models import Review, User, Answer


# class RegistrationForm(Form):
#     author_name = StringField('author-name', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


# class PostForm(FlaskForm):
#     id = IntegerField('id', validators=[DataRequired()])
#     author_name = StringField('author_name', validators=[DataRequired(), length(5, 55)])
#     review = TextAreaField(label='Review', validators=[DataRequired(), length(5, 2500)])
#     date_time = DateField('Date-Time', validators=[DataRequired()])
#     active = BooleanField('Available', validators=[DataRequired()])

# class UserForm(ModelForm):
#     class Meta:
#         model = User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        include = [
            'user_id',
        ]

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        include = [
            'review_id',
        ]
