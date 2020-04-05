from flask import request
from werkzeug.exceptions import BadRequest

from app.util import country_ip, verify_ip_format


def filtro_post(content_type):
    data = str(request.data).replace('b\'', '').replace('\'', '')
    if data is None or len(data) < 1:
        '''condicao para entrada vazia'''
        msg = 'Invalid Input! Entry cannot be empty'
        raise BadRequest(msg)

    texto = {}
    if 'text/plain' in content_type:
        split_request = [i.lstrip() for i in data.split(",")]
        if len(split_request) == 3:
            '''condicao para entrada: protocol, origin_ip, target_ip'''
            texto.update(protocol=split_request[0])
            texto.update(origin_ip=verify_ip_format(split_request[1]))
            texto.update(target_ip=verify_ip_format(split_request[2]))
            texto.update(origin_country=country_ip(split_request[1]))
        else:
            msg = 'Invalid Input! The entry must be a text/plain with content in this order: protocol, origin_ip, ' \
                  'target_ip '
            raise BadRequest(msg)

    elif 'application/json' in content_type:
        request_json = request.json

        try:
            texto.update(protocol=request_json['protocol'])
            texto.update(origin_ip=verify_ip_format(request_json['origin_ip']))
            texto.update(target_ip=verify_ip_format(request_json['target_ip']))
            texto.update(origin_country=country_ip(request_json['origin_ip']))
        except Exception:
            msg = 'Invalid Input! The entry must be JSON with keys: protocol, origin_ip and target_ip'
            raise BadRequest(msg)
    return texto
