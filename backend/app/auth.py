from flask import jsonify, request
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity

import datetime
from http import HTTPStatus

from app import app, db, mail
from app.models import User
from app.emails import *
from app.decorators import is_current_user, has_access_token, has_reset_pass_token


@app.route('/api/auth/register', methods=['POST'])
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if db.session.query(User).filter_by(userEmail=email).first() is not None:
        return jsonify(msg="That email is already in use."), HTTPStatus.BAD_REQUEST

    user = User(userEmail=email, userPass=generate_password_hash(password),
                createdOn=datetime.datetime.utcnow(), hasConfirmedEmail=False)
    db.session.add(user)
    db.session.commit()
    return jsonify(id=user.userID)


@app.route('/api/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = db.session.query(User).filter_by(userEmail=email).first()
    if not user.hasConfirmedEmail:
        return "Please confirm your email before logging in.", HTTPStatus.FORBIDDEN

    if user is None or not check_password_hash(user.userPass, password):
        return "Incorrect email or password.", HTTPStatus.BAD_REQUEST

    access_token = create_access_token(identity=user.userID)
    return jsonify(accessToken=access_token, hasConfirmedEmail=user.hasConfirmedEmail)


@app.route('/api/auth/reset-pass-request', methods=['POST'])
def reset_pass_request():
    email = request.json.get('email')
    user = db.session.query(User).filter_by(userEmail=email).first()
    if user is not None:
        token_type = {"type": "resetPassword"}
        reset_email_token = create_access_token(
            identity=user.userID, expires_delta=datetime.timedelta(hours=1), additional_claims=token_type)
        send_reset_pass_email(email, reset_email_token)

    # shows even if invalid email is entered to prevent checking if accounts exist
    return "A password reset link has been sent to " + email


def send_reset_pass_email(recipient, token):
    # TODO set default sender app setting
    msg = Message('Reset Your Password',
                  sender='ksucourseplanner@gmail.com', recipients=[recipient])
    msg.body = get_reset_password_txt(token)
    msg.html = get_reset_password_html(token)
    mail.send(msg)


@app.route('/api/auth/reset-pass', methods=['POST'])
@has_reset_pass_token()
def reset_pass():
    password = request.json.get('password')
    user = db.session.query(User).get(get_jwt_identity())
    if user is not None:
        user.userPass = generate_password_hash(password)
        db.session.commit()

    else:
        # doubt this would happen but just in case the user gets deleted or something?
        return "Invalid token ID", HTTPStatus.INTERNAL_SERVER_ERROR

    return ("", HTTPStatus.NO_CONTENT)


# used for verifying token on new session
@app.route('/api/auth/verify/access')
@has_access_token()
def verify_access_token():
    return ("", HTTPStatus.NO_CONTENT)


@app.route('/api/auth/verify/reset-pass')
@has_reset_pass_token()
def verify_reset_pass_token():
    return ("", HTTPStatus.NO_CONTENT)


@app.route('/api/auth/confirm-email', methods=['POST'])
def confirm_email():
    user_id = request.json.get('userId')
    user = db.session.query(User).get(user_id)
    if user is None:
        return jsonify(msg="User with that ID does not exist."), HTTPStatus.BAD_REQUEST

    user.hasConfirmedEmail = True
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
