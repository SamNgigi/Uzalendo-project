import os


class Config:
    """
    Parent Config
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:Sam@localhost/mzalendo'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Child Config with production configurations
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # pass


class DevConfig(Config):
    """
    Child Config with development configurations
    """
    DEBUG = True


class TestConfig(Config):
    """
    Child Config with test configurations
    """
    pass


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}
