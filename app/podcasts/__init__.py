from flask import Blueprint

bp = Blueprint('podcasts', __name__)

from app.podcasts import routes