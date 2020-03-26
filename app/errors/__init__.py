from flask import Blueprint

errors = Blueprint('erroes', __name__)

from . import errors
