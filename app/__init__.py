from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
db = SQLAlchemy()
# photos = UploadSet('photos', IMAGES)
# # media  = UploadSet('videos, default_dest=videos)


def create_app(config_name):
    app = Flask(__name__)
    # creates apps congifurations
    # app.config.from_object(config_options[config_name])

    # initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # # configure UploadSet
    # configure_uploads(app, photos)

    return app
