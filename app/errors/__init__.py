from flask import Blueprint

from app import app

errors = Blueprint('erroes', __name__)

from . import errors
