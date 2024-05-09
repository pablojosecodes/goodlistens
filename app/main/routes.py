import flask 
from flask import url_for
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RecommendForm
from flask import request, url_for, abort

from app.main import bp

@bp.route("/")
@bp.route("/index")
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user, active_page="home", testing=True)

@bp.route("/home")
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', user=user)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main.index'))
    return render_template('forms/login.html', title='Sign In', form=form)

@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Feedback submitted!')
        return redirect(url_for('main.index'))
    return render_template('forms/feeedback.html', title='Feedback', form=form)


@bp.route("/recommend", methods=["GET", "POST"])
def recommend():
    form = RecommendForm()
    if form.validate_on_submit():
        flash(f"Successfully submitted!")

        return redirect(url_for("recommend") +"?success=True")
    return render_template('forms/recommend.html', title="Recommend Podcast", form=form)
