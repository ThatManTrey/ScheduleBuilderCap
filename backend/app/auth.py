from flask import jsonify, request
from flask_mail import Mail, Message
from app import app, db, mail
from app.models import User
import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from app.emails import *


# decorator to check if user making the request is the same as
#   the requested user to get information about
# add @is_current_user to any endpoint that returns user information
def is_current_user(function):
    def wrapper(user_id):
        if get_jwt_identity() != user_id:
            return jsonify(msg="You cannot access another user's information."), 403
        return function(user_id)
    return wrapper


@app.route('/api/auth/register', methods=['POST'])
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if db.session.query(User).filter_by(userEmail=email).first() is not None:
        return jsonify(msg="That email is already in use."), 400

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

    if user is None or not check_password_hash(user.userPass, password):
        return jsonify(msg="Incorrect email or password."), 400

    access_token = create_access_token(identity=user.userID)
    return jsonify(access_token=access_token)


@app.route('/api/auth/reset-pass-request', methods=['POST'])
def reset_pass_request():
    email = request.json.get('email')
    user = db.session.query(User).filter_by(userEmail=email).first()
    if user is not None:
        token_type = {"type": "resetPassword"}
        reset_email_token = create_access_token(identity=user.userID, expires_delta=datetime.timedelta(hours=1), additional_claims=token_type)
        send_reset_pass_email(email, reset_email_token)

    # shows even if invalid email is entered to prevent checking if accounts exist
    return "A password reset link has been sent to " + email


@app.route('/api/auth/reset-pass', methods=['POST'])
@jwt_required()
def reset_pass():
    if get_jwt()['type'] != "resetPassword":
        return "Invalid token type", 403
    
    password = request.json.get('password')
    user = db.session.query(User).get(get_jwt_identity())
    if user is not None:
        user.userPass = generate_password_hash(password)
        db.session.commit()

    return ("", 204)


def send_reset_pass_email(recipient, token):
    # TODO set default sender app setting
    msg = Message('Reset Your Password',
                  sender='ksucourseplanner@gmail.com', recipients=[recipient])
    msg.body = get_reset_password_txt(token)
    msg.html = get_reset_password_html(token)
    mail.send(msg)


# used for verifying token on new session
@app.route('/api/auth/verify/access')
@jwt_required()
def verify_access_token():
    if get_jwt()['type'] != "access":
        return "Invalid token type", 403
    return ("", 204)


@app.route('/api/auth/verify/reset-pass')
@jwt_required()
def verify_reset_pass_token():
    if get_jwt()['type'] != "resetPassword":
        return "Invalid token type", 403
    return ("", 204)


@app.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()
@is_current_user
def get_user(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        return jsonify(msg="User with that ID does not exist."), 400

    return jsonify(userID=user.userID, userEmail=user.userEmail, createdOn=user.createdOn)
