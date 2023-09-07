#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
# from api.v1.views.users import *
# Code section commented because of circular imort error
# from api.v1.views.index import *
from models.user import User
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


User.load_from_file()
