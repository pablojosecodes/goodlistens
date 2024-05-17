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

    from app.podcasts import bp as podcasts_bp
    app.register_blueprint(podcasts_bp)

    from app.feedback import bp as feedback_dp
    app.register_blueprint(feedback_dp)

    from app.auth import bp as auth_dp
    app.register_blueprint(auth_dp)


    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    # ... no changes to blueprint registration
    # with app.app_context():
    #     db.create_all()  #
    #     from app.models import Podcast

    #     # Add podcasts
    #     podcast1 = Podcast(
    #         name="My First Million",
    #         id="HS2300184645",
    #         rss="https://feeds.megaphone.fm/HS2300184645",
    #         image="https://megaphone.imgix.net/podcasts/39846662-79ea-11eb-9b06-a75ddc4bddcc/image/MFM_ShowTile_2024.png",
    #         website="https://mfmpod.com",
    #         description="Parr and Shaan Puri brainstorm new business ideas based on trends & opportunities they see in the market. Sometimes they bring on famous guests to brainstorm with them."
    #     )

    #     podcast2 = Podcast(
    #         name="Sean Carroll's Mindscape",
    #         id="sean-carrolls-mindscape",
    #         rss="https://rss.art19.com/sean-carrolls-mindscape",
    #         image="https://content.production.cdn.art19.com/images/33/9d/14/7c/339d147c-92a1-4845-b785-1533a47d5929/21d641ef836c48dff270cbede4360d187bdd6c56cb126be7d6f51078db34d4675527fa72e13c86bb573ec42c5d4fc493e18e7d95fec734ec77168fc379baefcf.jpeg",
    #         website="https://www.preposterousuniverse.com/podcast",
    #         description="Ever wanted to know how music affects your brain, what quantum mechanics really is, or how black holes work? Do you wonder why you get emotional each time you see a certain movie, or how on earth video games are designed? Then you've come to the right place. Each week, Sean Carroll will host conversations with some of the most interesting thinkers in the world. From neuroscientists and engineers to authors and television producers, Sean and his guests talk about the biggest ideas in science, philosophy, culture and much more."
    #     )

    #     db.session.add(podcast1)       
    #     db.session.add(podcast2)
    #     db.session.commit()

        # Add episodes from a list of dictionaries
        # episodes_data = [
        #     # ... (keep the existing episodes_data list        ]

        # for episode_data in episodes_data:
        #     episode = Episode(
        #         id=episode_data['id'],                date=episode_data['date'],
        #         title=episode_data['title'],
        #         image=episode_data['image'],
        #         duration=episode_data['duration'],
        #         description=episode_data['description'],
        #         podcast_id=episode_data['podcast_id']
        #     )
        #     db.session.add(episode)

        # db.session.commit()
        # print("COMMITTED")


    # if not app.debug and not app.testing:
        # ... no changes to logging setup

    return app



from app import models
