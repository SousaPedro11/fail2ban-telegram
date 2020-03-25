import os

from flask import request
from flask_restful import Resource
from telegram import Bot

from app.telegram import filters
from app.util import get_ip, country_ip

chat_id = os.environ.get('CHAT_ID')
token = os.environ.get('TOKEN')
bot = Bot(token=str(token))


class Telegram(Resource):

    def get(self):
        ip = get_ip(request)
        texto = country_ip(ip)
        texto.update(user_agent=request.user_agent.string)
        bot.send_message(chat_id=chat_id, text=texto)
        return texto

    def post(self):
        req = request.content_type
        texto = filters.filtro_post(req)

        texto = dict(sorted(texto.items(), key=lambda x: x[0]))

        bot.send_message(chat_id=chat_id, text=texto)
        return texto
