from flask import jsonify, request
from flask_jwt_extended import get_jwt, get_jwt_identity, verify_jwt_in_request

from functools import wraps
from http import HTTPStatus
import os
import jwt
import time

from app.models import User
from app import app, db


# decorator to check if user making the request is the same as
#   the requested user to get information about
# add @is_current_user() to any endpoint that returns user information
# endpoint must take <int:user_id> in params
def is_current_user():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if kwargs['user_id'] != get_jwt_identity():
                return jsonify(msg="You cannot access another user's information."), HTTPStatus.FORBIDDEN

            return fn(*args, **kwargs)

        return decorator
    return wrapper


def has_access_token(optional=False):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request(optional)

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
            token = request.headers.get('Authorization')

            if not token:
                return "No token found", HTTPStatus.UNAUTHORIZED
            
            # decode token without verifying first to get userID
            try:
                token_payload = jwt.decode(token, options={"verify_signature": False}, algorithms="HS256")
            except:
                return "Invalid token", HTTPStatus.UNPROCESSABLE_ENTITY

            if token_payload['type'] != "resetPassword":
                return "Invalid token type", HTTPStatus.FORBIDDEN
            if time.time() > token_payload['exp']:
                return "Token has expired", HTTPStatus.UNPROCESSABLE_ENTITY

            user = db.session.query(User).get(token_payload['sub'])
            if user is None:
                return "User with that ID does not exist", HTTPStatus.NOT_FOUND

            # finally verify the token with the user's current hashed password
            verified_token = jwt.decode(token, user.userPass, algorithms="HS256")
            return fn(*args, **kwargs)

        return decorator
    return wrapper


def has_confirmation_token():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request(locations=["headers"])

            if get_jwt()['type'] == "confirmEmail":
                return fn(*args, **kwargs)
            else:
                return "Invalid token type", HTTPStatus.FORBIDDEN

        return decorator
    return wrapper


