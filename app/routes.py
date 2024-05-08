import flask 
from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user, active_page="home", testing=True)


@app.route("/home")
def home():
    return render_template('index.html')