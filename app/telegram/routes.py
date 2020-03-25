from app import api
from app.telegram.models import Telegram

api.add_resource(Telegram, "/telegram/", "/index/", "/", endpoint="telegram")
