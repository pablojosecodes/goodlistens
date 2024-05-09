from app import db
from app.models import User

from sqlalchemy import select
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, URLField, EmailField
from wtforms.validators import DataRequired, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Password", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    about = TextAreaField("About Me")
    remember_me = BooleanField("Remember Me?")
    submit = SubmitField("Sign In")
    
    
    def validate_username(self, username):
        user = db.session.scalar(select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError(('Please use a different username.'))

    def validate_email(self, email):
        user = db.session.scalar(select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError(('Please use a different email address.'))



class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    about = TextAreaField("About Me")
    remember_me = BooleanField("Remember Me?")
    submit = SubmitField("Sign In")