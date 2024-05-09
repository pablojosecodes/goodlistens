from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    about = TextAreaField("About Me")
    remember_me = BooleanField("Remember Me?")
    submit = SubmitField("Sign In")

class RecommendForm(FlaskForm):
    name = StringField("Podcast Name", validators=[DataRequired()])
    rssfeed = URLField("RSS Feed URL", validators=[DataRequired()])
    about = TextAreaField("(Optional) Description")
    submit = SubmitField("Submit")