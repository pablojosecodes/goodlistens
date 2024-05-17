from flask import url_for, request
from flask import render_template, flash, redirect
from app.feedback.forms import  RecommendForm
from flask import  url_for
from sqlalchemy import select
from app.models import User
from flask_login import  current_user, login_required
from app.podcasts import bp
from app import db



@bp.route('/movie')
def moviek():
    # user = User.query.filter_by(username=username).first()
    # if user is None:
    #     flash('User {} not found.'.format(username))
    #     return redirect(url_for('main.home'))
    # if current_user.is_following(user):
    #     flash('You are already following this user.')
    #     return redirect(url_for('main.user_profile'))
    # current_user.follow(user)
    # db.session.commit()
    # flash('You are now following {}.'.format(username))
    return render_template('home.html', user=current_user)


@bp.route('/success/<int:name>')
def success(name):
    # return 'welcome %s' % name
    return render_template('home.html', user=current_user)



@bp.route('/movie/<movie_id>')
def movie(movie_id):
    # user = User.query.filter_by(username=username).first()
    # if user is None:
    #     flash('User {} not found.'.format(username))
    #     return redirect(url_for('main.home'))
    # if current_user.is_following(user):
    #     flash('You are already following this user.')
    #     return redirect(url_for('main.user_profile'))
    # current_user.follow(user)
    # db.session.commit()
    # flash('You are now following {}.'.format(username))
    return render_template('home.html', user=current_user)


