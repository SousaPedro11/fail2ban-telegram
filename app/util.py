from ipaddress import ip_address

import requests
from werkzeug.exceptions import BadRequest


def get_ip(request):
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return ip


def data_from_ip(ip) -> dict:
    r = requests.get('http://ip-api.com/json/' + ip)
    parsed_json = r.json()

    texto = {'country': parsed_json['country'], 'regionName': parsed_json['regionName'], 'city': parsed_json['city']} \
        if 'country' in parsed_json.keys() else {'status': parsed_json["status"], 'message': parsed_json["message"]}

    return texto


def verify_ip_format(ip):
    try:
        result = ip_address(ip).__str__()
    except ValueError as e:
        raise BadRequest(f'Invalid input. {str(e)}')
    return result


def verify_protocol(protocol):
    if protocol.isdecimal():
        raise BadRequest(f'Invalid input. Protocol must be a string')
    return protocol
