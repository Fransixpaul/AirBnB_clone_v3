#!/usr/bin/python3
"""
create Flask app and register the blue print app_views to flask instance app/
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
