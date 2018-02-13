from flask import Blueprint
main = Blueprint('auth', __name__)
from . import views, forms
