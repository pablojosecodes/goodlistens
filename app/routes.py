import flask 
from flask import url_for
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RecommendForm
from flask import request, url_for, abort


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user, active_page="home", testing=True)


@app.route("/home")
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    form = RecommendForm()
    if form.validate_on_submit():
        flash(f"Successfully submitted!")

        return redirect(url_for("recommend") +"?success=True")
    return render_template('recommend.html', title="Recommend Podcast", form=form)
