from flask import Flask
from flask_restful import Api

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

api = Api(app)

# Registra a Blueprint de HTTPAuth
from app.authorization import http_auth

app.register_blueprint(http_auth)

# Registra a Blueprint da aplicacao central
from app.telegram import telegram_restful

app.register_blueprint(telegram_restful)

# Registra a Blueprint do errorhandler
from app.errors import errors

app.register_blueprint(errors)

# Registra a Blueprint do monitoringdashboard
from app.dashboard import dash

app.register_blueprint(dash)
