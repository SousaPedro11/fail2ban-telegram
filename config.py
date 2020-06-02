import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    load_dotenv(os.path.join(basedir, '.env'))
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    HTTPAUTH_USER = os.environ.get('HTTPAUTH_USER')
    HTTPAUTH_PASS = os.environ.get('HTTPAUTH_PASS')


class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class Testing(Config):
    TESTING = True


class Production(Config):
    load_dotenv(os.path.join(basedir, '.telegram'))  
    TOKEN = os.environ.get('TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')
    
    
config = {
    'dev': Development,
    'test': Testing,
    'prod': Production,
}
