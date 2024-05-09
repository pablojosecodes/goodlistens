import flask 
from flask import url_for
from flask import render_template, flash, redirect
from app import app
from app import db
from app.forms import LoginForm, RecommendForm, RegistrationForm
from flask import request, url_for, abort

from flask_login import login_user, current_user, logout_user
import sqlalchemy as sa
from app.models import User
from app.main import bp



@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', user=current_user)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = db.session.scalar(
    #         sa.select(User).where(User.username == form.username.data))
    #     if user is None or not user.check_password(form.password.data):
    #         flash(_('Invalid username or password'))
    #         return redirect(url_for('auth.login'))
    #     login_user(user, remember=form.remember_me.data)
    #     next_page = request.args.get('next')
    #     if not next_page or urlsplit(next_page).netloc != '':
    #         next_page = url_for('main.home')
    #     return redirect(next_page)
    # return render_template('auth/login.html', title=_('Sign In'), form=form)

    # if current_user.is_authenticated:
    #     return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Invalid login. Try again.")
            return redirect(url_for("main.login"))
        login_user(user, remember=form.remember_me.data)
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main.home'))
    return render_template('forms/login.html', title='Sign In', form=form)

@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Feedback submitted!')
        return redirect(url_for('main.home'))
    return render_template('forms/feeedback.html', title='Feedback', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))



@bp.route("/recommend", methods=["GET", "POST"])
def recommend():
    form = RecommendForm()
    if form.validate_on_submit():
        flash(f"Successfully submitted!")

        return redirect(url_for("recommend") +"?success=True")
    return render_template('forms/recommend.html', title="Recommend Podcast", form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(('Congratulations, you are now a registered user!'))
        return redirect(url_for('main.login'))
    return render_template('forms/register.html', title=('Register'),
                           form=form)

