from flask import url_for, redirect, jsonify, request

from app import app
from app.util import get_ip


@app.route('/index/')
@app.route('/')
def index():
    return redirect(url_for('fail2ban'))


@app.route('/fail2ban/<argumento>/')
@app.route('/fail2ban/')
def fail2ban(argumento=None):
    if argumento:
        print(argumento)
        result = f'fail2ban startado! Args: {argumento}'
    else:
        result = 'fail2ban startado!'
    return result


@app.route("/get_my_ip/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': get_ip(request)})

# api.add_resource()
