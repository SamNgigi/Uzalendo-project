from flask import Flask
from flask_bootstrap import Bootstrap
from flask_uploads import uploadSet,configure_uploads,IMAGES,MEDIA

bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
media  = UploadSet('media', default_dest=videos app: app.instance_root)


def create_app(config_name):
    app = Flask(__name__)
    # creates apps congifurations
    app.config.from_object(config_options[config_name])

    # initialize flask extensions
    bootstrap.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # configure UploadSet
    configure_uploads(app, (photos, media))

    return app
