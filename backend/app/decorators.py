from flask import jsonify, request
from flask_jwt_extended import get_jwt, get_jwt_identity, verify_jwt_in_request
from functools import wraps
from http import HTTPStatus
from app import app
import os


# decorator to check if user making the request is the same as
#   the requested user to get information about
# add @is_current_user to any endpoint that returns user information
def is_current_user(function):
    def wrapper(user_id):
        if get_jwt_identity() != user_id:
            return jsonify(msg="You cannot access another user's information."), HTTPStatus.FORBIDDEN
        return function(user_id)
    return wrapper

def has_api_key():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if os.environ['FLASK_ENV'] == "development":
                return fn(*args, **kwargs)
            
            if "Api-Key" not in request.headers:
                return "API Key is required", HTTPStatus.BAD_REQUEST
            elif request.headers["Api-Key"] != app.config['SECRET_KEY']:
                return "Invalid API Key", HTTPStatus.BAD_REQUEST
            else:
                 return fn(*args, **kwargs)
        return decorator
    return wrapper


def has_access_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if get_jwt()['type'] == "access":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.FORBIDDEN

        return decorator
    return wrapper


def has_reset_pass_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if get_jwt()['type'] == "resetPassword":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.FORBIDDEN

        return decorator
    return wrapper


def has_confirmation_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if get_jwt()['type'] == "confirmEmail":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.FORBIDDEN

        return decorator
    return wrapper