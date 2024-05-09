from app import db
from app.models import User

from sqlalchemy import select
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, URLField, EmailField
from wtforms.validators import DataRequired, ValidationError


class RecommendForm(FlaskForm):
    name = StringField("Podcast Name", validators=[DataRequired()])
    rssfeed = URLField("RSS Feed URL", validators=[DataRequired()])
    about = TextAreaField("(Optional) Description")
    submit = SubmitField("Submit")

class FeedbackForm(FlaskForm):
    feedback = TextAreaField("Feedback")
    submit = SubmitField("Submit")