import os

from flask import current_app
from telegram import Bot

chat_id = os.environ.get('CHAT_ID')
token = os.environ.get('TOKEN')
bot = Bot(token=str(token))


def send_message(texto) -> None:
    if not current_app.debug and not current_app.testing:
        bot.send_message(chat_id=chat_id, text=texto)
