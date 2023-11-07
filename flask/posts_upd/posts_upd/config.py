# host = 'LocalHost'
# port = '5500'
# DEBUG = True
# SECRET_KEY = 'I am a secret key'
#
# SQLALCHEMY_DATABASE_URI = 'sqlite:///post.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# WTF_CSRF_ENABLED = False


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    DEVELOPMENT = True
    SECRET_KEY = 'ICAO'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-posts.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False


class DevelopConfig(Config):
    DEBUG = True

