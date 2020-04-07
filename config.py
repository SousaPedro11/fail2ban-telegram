import os

from dotenv import set_key

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    set_key(os.path.join(basedir, '.env'), 'FLASK_ENV', 'production')


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
