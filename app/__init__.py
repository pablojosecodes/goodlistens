from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
# login.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.feedback import bp as feedback_dp
    app.register_blueprint(feedback_dp)

    from app.auth import bp as auth_dp
    app.register_blueprint(auth_dp)


    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    # ... no changes to blueprint registration

    # if not app.debug and not app.testing:
        # ... no changes to logging setup

    return app



from app import models
