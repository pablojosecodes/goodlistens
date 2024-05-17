from flask import url_for, request
from flask import render_template, flash, redirect
from app.feedback.forms import  RecommendForm
from flask import  url_for
from sqlalchemy import select
from app.models import User
from flask_login import  current_user, login_required
from app.main import bp
from app import db


@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def home():
    return render_template('home.html', user=current_user)

@bp.route("/users")
@login_required
def users():
    query = select(User)
    following = request.args.get('following')
    print(following)

    if following:
        # Filter users based on the "following" condition
        # query = query.where(User.following == True)
        current_user_id = current_user.id
        query = query.where(User.followers.any(User.id == current_user_id))

    users = db.session.scalars(query).all()
    return render_template('users.html', title='Explore', users=users)



@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.home'))
    if current_user.is_following(user):
        flash('You are already following this user.')
        return redirect(url_for('main.user_profile'))
    current_user.follow(user)
    db.session.commit()
    flash('You are now following {}.'.format(username))
    return redirect(url_for('main.users'))


@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if not current_user.is_following(user):
        flash('You are not following this user.')
        return redirect(url_for('user_profile'))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are no longer following {}.'.format(username))
    return redirect(url_for('main.users'))
