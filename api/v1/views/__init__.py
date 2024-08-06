#!/usr/bin/python3
""" Create a flask app"""
from flask import Blueprint

app.view = Blueprint('app_views', __name__, url_prefix='/api.v1')

from api.v1.views.index import *
