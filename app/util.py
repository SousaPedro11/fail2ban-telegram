import re

import requests
from flask import request
from werkzeug.exceptions import BadRequest


def get_ip(request):
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return ip


def country_ip(ip):
    r = requests.get('http://ip-api.com/json/' + ip)
    parsed_json = r.json()

    texto = parsed_json[
        'country'] if 'country' in parsed_json.keys() else f'{parsed_json["status"]}, {parsed_json["message"]}'

    return texto


def find_in_request(filtro):
    return re.compile(filtro).findall(str(request.data))


def verify_ip_format(ip):
    filtro = '\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}'
    findall = re.compile(filtro).findall(ip)
    if not findall:
        raise BadRequest(f'invalid ip {ip} in post data')
    return findall[0]
