from flask import request
from werkzeug.exceptions import BadRequest

from app.util import find_in_request, country_ip, verify_ip_format


def filtro_post(content_type):
    data = str(request.data).replace('b\'', '').replace('\'', '')
    if data is None or len(data) < 1:
        '''condicao para entrada vazia'''
        raise BadRequest('Ivalid Input')
        # return {'protocol': '', 'origin_ip': '', 'target_ip': ''}

    if 'text/plain' in content_type:
        split_request = [i.lstrip() for i in data.split(",")]
        if len(split_request) > 2:
            '''condicao para entrada: protocol, attacker_ip, target_ip'''
            texto = {}
            texto.update(protocol=split_request[0])
            texto.update(origin_ip=verify_ip_format(split_request[1]))
            texto.update(target_ip=verify_ip_format(split_request[2]))
            texto.update(country_origin=country_ip(split_request[1]))
            return texto

        '''caso a entrada seja a linha de log do fail2ban'''
        ip = find_in_request('\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}')
        notice = find_in_request('\w+\s+\[+\D+\]')
        date = find_in_request('\d{1,4}-\d{1,2}-\d{1,2}')
        hour = find_in_request('\d{1,2}:\d{1,2}:\d{1,2},\d{3}')
        if not ip:
            raise BadRequest('invalid IP in post data')
        texto = {}
        texto.update(ip=ip[0])
        texto.update(country=country_ip(ip[0]))
        texto.update(notice=notice[0] if notice else '')
        texto.update(status='Ban' if 'Ban' in data else 'unbanned' if 'Unban' in data else '')
        texto.update(date=date[0] if date else '')
        texto.update(hour=hour[0] if hour else '')

    elif 'application/json' in content_type:
        request_json = request.json
        texto = {}
        texto.update(country_ip(request_json['ip'])) if 'ip' in request_json.keys() else ''

        try:
            texto.update(protocol=request_json['protocol'])
            texto.update(origin_ip=request_json['origin_ip'])
            texto.update(target_ip=request_json['target_ip'])
            texto.update(country_origin=country_ip(request_json['origin_ip']))
        except Exception:
            raise BadRequest(
                'argumentos invalidos! Deve ser '
                '{'
                '"protocol": "protocol_name",'
                ' "origin_ip": "ip",'
                ' "target_ip": "ip"'
                '}')
    return texto
