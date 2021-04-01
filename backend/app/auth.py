from flask import jsonify, request, make_response
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies, unset_jwt_cookies, get_jwt, get_current_user

from datetime import datetime, timezone, timedelta
import jwt
from http import HTTPStatus
import time

from app import app, db, mail
from app.models import User
from app import jwt as jwt_extended
from app.emails import *
from app.decorators import is_current_user, has_access_token, has_reset_pass_token, has_confirmation_token, has_api_key


#
# ------------------------ USER ACCOUNTS ----------------------------------
#


@app.route('/api/auth/register', methods=['POST'])
@has_api_key()
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if db.session.query(User).filter_by(userEmail=email).first() is not None:
        return jsonify(msg="That email is already in use."), HTTPStatus.BAD_REQUEST

    user = User(userEmail=email, userPass=generate_password_hash(password),
                createdOn=datetime.now(timezone.utc), hasConfirmedEmail=False)
    db.session.add(user)
    db.session.commit()

    token_type = {"type": "confirmEmail"}
    confirm_email_token = create_access_token(
        identity=user.userID, expires_delta=False, additional_claims=token_type)
    send_confirmation_email(user.userEmail, confirm_email_token)

    return jsonify(id=user.userID)


@app.route('/api/auth/login', methods=['POST'])
@has_api_key()
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = db.session.query(User).filter_by(userEmail=email).first()

    if user is None or not check_password_hash(user.userPass, password):
        return "Incorrect email or password.", HTTPStatus.BAD_REQUEST

    access_token = create_access_token(identity=user.userID)
    response = jsonify(hasConfirmedEmail=bool(
        user.hasConfirmedEmail), userId=user.userID)
    set_access_cookies(response, access_token)
    return response


@app.route('/api/auth/logout', methods=['POST'])
@has_api_key()
def logout():
    response = jsonify(msg="Logout successful")
    unset_jwt_cookies(response)
    return response


#
# ------------------------ EMAILS ----------------------------------
#


def send_confirmation_email(recipient, token):
    msg = Message('Confirm Your Account', recipients=[recipient])
    msg.body = get_confirm_email_txt(token)
    msg.html = get_confirm_email_html(token)
    mail.send(msg)


@app.route('/api/auth/resend-confirm', methods=['POST'])
@has_api_key()
@has_access_token()
def resend_confirm_email():
    user = get_current_user()

    token_type = {"type": "confirmEmail"}
    confirm_email_token = create_access_token(identity=user.userID,
                                              expires_delta=False, additional_claims=token_type)

    send_confirmation_email(user.userEmail, confirm_email_token)
    return "Email has been sent"


@app.route('/api/auth/reset-pass-request', methods=['POST'])
@has_api_key()
def reset_pass_request():
    email = request.json.get('email')
    user = db.session.query(User).filter_by(userEmail=email).first()
    if user is not None:
        # have to use PyJWT here since this token will have a different signature from the others
        reset_pass_token = jwt.encode(
            {
                "exp": datetime.utcnow() + timedelta(hours=1),
                "type": "resetPassword",
                "sub": user.userID
            },
            user.userPass,      # sign the token with the user's current hashed password
                                # prevents reset password links from being used multiple times
            algorithm="HS256"
        )

        send_reset_pass_email(email, reset_pass_token)

    # shows even if invalid email is entered to prevent checking if accounts exist
    return "A password reset link has been sent to " + email


def send_reset_pass_email(recipient, token):
    msg = Message('Reset Your Password', recipients=[recipient])
    msg.body = get_reset_password_txt(token)
    msg.html = get_reset_password_html(token)
    mail.send(msg)


@app.route('/api/auth/reset-pass', methods=['POST'])
@has_api_key()
@has_reset_pass_token()
def reset_pass():
    token = request.headers.get('Authorization')
    token_payload = jwt.decode(
        token, options={"verify_signature": False}, algorithms="HS256")

    user = db.session.query(User).get(token_payload['sub'])
    if user is not None:
        password = request.json.get('password')
        user.userPass = generate_password_hash(password)
        user.lastPasswordReset = datetime.now()
        db.session.commit()
    else:
        # shouldn't happen in production unless account deletion is implemented
        return "User does not exist", HTTPStatus.NOT_FOUND

    return ("", HTTPStatus.NO_CONTENT)


#
# ------------------------ TOKEN VERIFICATION ----------------------------------
#


# used for verifying existing access token on new session
@app.route('/api/auth/verify/access')
@has_api_key()
@has_access_token()
def verify_access_token():
    user = get_current_user()
    return jsonify(hasConfirmedEmail=bool(user.hasConfirmedEmail), userId=user.userID)


# needed for routing check
@app.route('/api/auth/verify/reset-pass')
@has_api_key()
@has_reset_pass_token()
def verify_reset_pass_token():
    return ("", HTTPStatus.NO_CONTENT)


# needed for routing check
@app.route('/api/auth/verify/confirm')
@has_api_key()
@has_confirmation_token()
def verify_confirmation_token():
    user = get_current_user()
    if user.hasConfirmedEmail:
        return "Email has already been confirmed", HTTPStatus.BAD_REQUEST

    user.hasConfirmedEmail = True
    db.session.commit()

    return ("", HTTPStatus.NO_CONTENT)


#
# ---------------------- JWT EXTENDED CALLBACKS --------------------------------
#


@jwt_extended.user_lookup_loader
def lookup_user(jwt_headers, jwt_payload):
    user = db.session.query(User).get(jwt_payload['sub'])
    if not user:
        return None

    return user


@jwt_extended.user_lookup_error_loader
def lookup_user_error(jwt_headers, jwt_payload):
    return "User not found", HTTPStatus.NOT_FOUND


# two possibilities for access tokens
#   1. the token has expired and the user hasn't yet reset their password,
#       or they reset it before the token was created. Generate new token and
#       return 470 status to let the client retry
#   2. the token was created before the user's last password reset, return 471 status,
#       remove cookies and force user to login again
#
# In general, the user should never have to login after the first time unless they
# invalidate their token or reset their password
@jwt_extended.expired_token_loader
def refresh_expired_access_tokens(jwt_header, jwt_payload):
    if jwt_payload['type'] != 'access':
        return "Token has expired", HTTPStatus.UNPROCESSABLE_ENTITY

    user = db.session.query(User).get(jwt_payload['sub'])
    if not user:
        # shouldn't happen in production unless account deletion is implemented
        return "User does not exist", HTTPStatus.NOT_FOUND

    reset_timestamp = -1
    if user.lastPasswordReset:
        reset_timestamp = datetime.timestamp(user.lastPasswordReset)

    creation_timestamp = jwt_payload["exp"] - app.config['JWT_ACCESS_TOKEN_EXPIRES'].total_seconds()

    if creation_timestamp > reset_timestamp:
        access_token = create_access_token(identity=jwt_payload['sub'])
        response = make_response("Access token has been refreshed", 470)
        set_access_cookies(response, access_token)
        debug_expired_jwts(True, creation_timestamp, jwt_payload["exp"], user.lastPasswordReset)
    else:
        response = make_response("Access token has expired", 471)
        unset_jwt_cookies(response)
        debug_expired_jwts(False, creation_timestamp, jwt_payload["exp"], user.lastPasswordReset)

    return response


def debug_expired_jwts(has_refreshed, creation_timestamp, expires_timestamp, lastPasswordReset):
    if app.config['DEBUG']:
        print("--------------EXPIRED JWTS----------------------")
        print("Token created on \t", datetime.fromtimestamp(creation_timestamp))
        print("Current time \t\t", datetime.now())
        print("Token expired on \t", datetime.fromtimestamp(expires_timestamp))
        print("Last password reset \t", lastPasswordReset)
        if(has_refreshed):
            print("New token has been created")
        else:
            print("Token has expired")
        print("--------------------------------------------")
