import os

from dotenv import load_dotenv, set_key

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    set_key(os.path.join(basedir, '.env'), 'FLASK_ENV', 'production')


class Development(Config):
    DEBUG = True
    set_key(os.path.join(basedir, '.env'), 'FLASK_ENV', 'development')


class Testing(Config):
    TESTING = True
