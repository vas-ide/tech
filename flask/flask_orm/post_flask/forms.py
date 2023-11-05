from wtforms_alchemy import ModelForm

from tech.flask.flask_orm.post_flask.models import GuessBookItem


# class PostForm(FlaskForm):
#     id = IntegerField(label='ID', validators=[DataRequired()])
#     review = TextAreaField(label='Review', validators=[DataRequired(), length(5, 2500)])


class PostForm(ModelForm):
    class Meta:
        model = GuessBookItem
