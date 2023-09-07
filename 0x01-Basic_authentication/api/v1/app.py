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


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorised(error) -> str:
    """ Unautorised handler
    """
    return jsonify({"error": "Unauthorised"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden Handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_any_request():
    """ This function runs before any request is made
        to the API Application
    """
    reqs = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth is None:
        return
    for url in reqs:
        if auth.require_auth(request.path, url) is True:
            return
    # if any(auth.require_auth(request.path, url) for url in reqs):
    #    return
    if auth.authorization_header(request) is None:
        return abort(401)
    if auth.current_user(request) is None:
        return abort(403)


if __name__ == "__main__":
    """
    Main entry point for the application.

    Reads the environment variables for the API host and port,
    and the authentication type.

    If authentication is enabled, imports the Auth class from
    the api.v1.auth.auth module.
    Starts the Flask app.
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    auth = getenv("AUTH_TYPE", 'auth')  # Look into here
    if auth:
        from api.v1.auth.auth import Auth
        auth = Auth()
    app.run(host=host, port=port)
