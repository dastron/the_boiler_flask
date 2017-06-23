import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = '##REPLACE##'
    PREFERRED_URL_SCHEME = ('http')

    CLIENT_ID = "##REPLACE"
    SQLALCHEMY_ECHO = False
    MAX_CONTENT_LENGTH = 36 * 1024 * 1024


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = '##REPLACE'


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///boiler.db'


class TestingConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = '##REPLACE'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig()
}
