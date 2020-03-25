from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

from app.telegram.models import Telegram

http_auth = Blueprint('http_auth', __name__)

auth = HTTPBasicAuth()

from . import auth_impl

Telegram.method_decorators.append(auth.login_required)
