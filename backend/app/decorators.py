from flask import jsonify, request
from flask_jwt_extended import get_jwt, get_jwt_identity, verify_jwt_in_request, unset_jwt_cookies
from functools import wraps
from http import HTTPStatus
from app.models import User
from app import app, db
import os
import jwt
import time

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
            # remove cookies from response if invalid
            try:
                verify_jwt_in_request(locations=['cookies'])
            except:
                response = jsonify(msg="Invalid token")
                unset_jwt_cookies(response)
                return response, HTTPStatus.UNPROCESSABLE_ENTITY

            user = db.session.query(User).get(get_jwt_identity())
            if user is None:
                return "User with that ID does not exist", HTTPStatus.UNAUTHORIZED

            if get_jwt()['type'] == "access":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.BAD_REQUEST

        return decorator
    return wrapper


def has_reset_pass_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return "No token found", HTTPStatus.UNAUTHORIZED
            
            # decode token without verifying first to get userID
            token_payload = jwt.decode(token, options={"verify_signature": False}, algorithms="HS256")

            if token_payload['type'] != "resetPassword":
                return "Invalid token type", HTTPStatus.UNAUTHORIZED
            if time.time() > token_payload['exp']:
                return "Token has expired", HTTPStatus.UNAUTHORIZED

            user = db.session.query(User).get(token_payload['sub'])
            if user is None:
                return "User with that ID does not exist", HTTPStatus.BAD_REQUEST

            # finally verify the token with the user's current hashed password
            verified_token = jwt.decode(token, user.userPass, algorithms="HS256")
            return fn(*args, **kwargs)

        return decorator
    return wrapper


def has_confirmation_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = db.session.query(User).get(get_jwt_identity())
            if user is None:
                return "User with that ID does not exist", HTTPStatus.UNAUTHORIZED

            if get_jwt()['type'] == "confirmEmail":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.FORBIDDEN

        return decorator
    return wrapper