from flask import url_for
from flask import render_template, flash, redirect
from app.feedback.forms import  RecommendForm
from flask import  url_for

from flask_login import  current_user
from app.main import bp


@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', user=current_user)
