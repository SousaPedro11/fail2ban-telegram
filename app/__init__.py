from flask import Flask
from flask_restful import Api
from config import config

from app.event.models import db as event_db

api = Api()


def create_app(config_name:str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    event_db.init_app(app)
    with app.app_context():
        event_db.create_all()
    
    # Registra a Blueprint de HTTPAuth
    from app.authorization import http_auth

    app.register_blueprint(http_auth)

    # Registra a Blueprint da aplicacao central
    from app.telegram import telegram_restful

    app.register_blueprint(telegram_restful)

    # Registra a Blueprint do errorhandler
    from app.errors import errors_bp

    app.register_blueprint(errors_bp)

    api.init_app(app)

    return app
