
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+pysopyg2://TevinMilla:3457hello@localhost/uzalendo'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    Debug = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

# class Config:
#     UPLOADED_PHOTOS_DEST = 'app/static/photos'
#     # UPLOADED_MEDIA_DEST = 'app/static/videos'
