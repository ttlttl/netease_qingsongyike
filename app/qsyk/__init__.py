from flask import Blueprint

qsyk = Blueprint('qsyk', __name__)

from . import views
