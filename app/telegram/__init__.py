from flask import Blueprint

telegram_restful = Blueprint('telegram_restful', __name__)

from . import routes
