from flask import url_for
from flask import render_template, flash, redirect
from app.feedback.forms import  RecommendForm
from flask import  url_for

from flask_login import  current_user
from app.main import bp


@bp.route("/recommend", methods=["GET", "POST"])
def recommend():
    form = RecommendForm()
    if form.validate_on_submit():
        flash(f"Successfully submitted!")
        return redirect(url_for("recommend") +"?success=True")
    return render_template('forms/recommend.html', title="Recommend Podcast", form=form)
