#!/usr/bin/env python3
"""
Route module for the API
"""


from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

authenticate = getenv("AUTH_TYPE")
if authenticate == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif authenticate == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif authenticate == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorised(error) -> str:
    """ Unautorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden Handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_any_request():
    """ This function runs before any request is made
        to the API Application
    Return:
        only authenticated user, otherise None
    """
    reqs = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth is None:
        return
    for url in reqs:
        if auth.require_auth(request.path, url) is False:
            return
    if auth.authorization_header(request) is None:
        return abort(401)

    current_usr = auth.current_user(request)
    if current_usr is None:
        return abort(403)
    else:
        request.current_user = current_usr


if __name__ == "__main__":
    """ run program
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    # authenticate = getenv("AUTH_TYPE")
    # if authenticate == 'auth':
    #    from api.v1.auth.auth import Auth
    #    auth = Auth()
    # if authenticate == 'basic_auth':
    #    from api.v1.auth.basic_auth import BasicAuth
    #    auth = BasicAuth()
    # if authenticate == 'session_auth':
    #    from api.v1.auth.session_auth import SessionAuth
    #    auth = SessionAuth()

    app.run(host=host, port=port)
