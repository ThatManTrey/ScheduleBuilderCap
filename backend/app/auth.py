from flask import jsonify, request
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies

import datetime
import jwt
from http import HTTPStatus

from app import app, db, mail
from app.models import User
from app.emails import *
from app.decorators import is_current_user, has_access_token, has_reset_pass_token, has_confirmation_token, has_api_key


@app.route('/api/auth/register', methods=['POST'])
@has_api_key()
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if db.session.query(User).filter_by(userEmail=email).first() is not None:
        return jsonify(msg="That email is already in use."), HTTPStatus.BAD_REQUEST

    user = User(userEmail=email, userPass=generate_password_hash(password),
                createdOn=datetime.datetime.utcnow(), hasConfirmedEmail=False)
    db.session.add(user)
    db.session.commit()

    token_type = {"type": "confirmEmail"}
    confirm_email_token = create_access_token(
        identity=user.userID, expires_delta=False, additional_claims=token_type)
    send_confirmation_email(user.userEmail, confirm_email_token)

    return jsonify(id=user.userID)


def send_confirmation_email(recipient, token):
    msg = Message('Confirm Your Account', recipients=[recipient])
    msg.body = get_confirm_email_txt(token)
    msg.html = get_confirm_email_html(token)
    mail.send(msg)


@app.route('/api/auth/login', methods=['POST'])
@has_api_key()
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = db.session.query(User).filter_by(userEmail=email).first()

    if user is None or not check_password_hash(user.userPass, password):
        return "Incorrect email or password.", HTTPStatus.BAD_REQUEST

    access_token = create_access_token(identity=user.userID)
    response = jsonify(accessToken=access_token, hasConfirmedEmail=user.hasConfirmedEmail)
    set_access_cookies(response, access_token)
    return response


@app.route('/api/auth/reset-pass-request', methods=['POST'])
@has_api_key()
def reset_pass_request():
    email = request.json.get('email')
    user = db.session.query(User).filter_by(userEmail=email).first()
    if user is not None:
        # have to use PyJWT here since this token will have a different signature from the others
        reset_pass_token = jwt.encode(
            { 
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
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
    token_payload = jwt.decode(token, options={"verify_signature": False}, algorithms="HS256")

    user = db.session.query(User).get(token_payload['sub'])
    if user is not None:
        password = request.json.get('password')
        user.userPass = generate_password_hash(password)
        db.session.commit()

    else:
        # doubt this would happen but just in case the user gets deleted or something?
        return "Invalid token ID", HTTPStatus.INTERNAL_SERVER_ERROR

    return ("", HTTPStatus.NO_CONTENT)


# used for verifying token on new session
@app.route('/api/auth/verify/access')
@has_api_key()
@has_access_token()
def verify_access_token():
    user = db.session.query(User).get(get_jwt_identity())
    return jsonify(hasConfirmedEmail=user.hasConfirmedEmail)


@app.route('/api/auth/verify/reset-pass')
@has_api_key()
@has_reset_pass_token()
def verify_reset_pass_token():
    return ("", HTTPStatus.NO_CONTENT)


@app.route('/api/auth/verify/confirm')
@has_api_key()
@has_confirmation_token()
def verify_confirmation_token():
    user = db.session.query(User).get(get_jwt_identity())
    if user.hasConfirmedEmail:
        return "Email has already been confirmed", HTTPStatus.BAD_REQUEST

    user.hasConfirmedEmail = True
    db.session.commit()
    
    return ("", HTTPStatus.NO_CONTENT)