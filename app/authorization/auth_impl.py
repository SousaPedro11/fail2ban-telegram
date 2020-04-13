import os

from werkzeug.exceptions import Unauthorized
from werkzeug.security import check_password_hash, generate_password_hash

from app.authorization import auth

__usuario = os.environ.get('HTTPAUTH_USER')
__senha = os.environ.get('HTTPAUTH_PASS')


@auth.verify_password
def verify_password(username, password):
    if username == __usuario:
        return check_password_hash(generate_password_hash(__senha), password)
    raise Unauthorized
