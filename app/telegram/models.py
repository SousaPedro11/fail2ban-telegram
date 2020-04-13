from flask import request, jsonify
from flask_restful import Resource

from app.telegram import filters
from app.telegram.bot import send_message
from app.util import get_ip, country_ip


class Telegram(Resource):

    def get(self):
        ip = get_ip(request)
        texto = {}
        texto.update(country_ip=country_ip(ip))
        texto.update(user_agent=request.user_agent.string)

        send_message(texto)

        return jsonify(texto)

    def post(self):
        request_type = request.content_type
        texto = filters.filtro_post(request_type)
        texto = dict(sorted(texto.items(), key=lambda x: x[0]))

        send_message(texto)

        return jsonify(texto)
