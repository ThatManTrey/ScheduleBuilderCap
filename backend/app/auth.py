from flask import jsonify, request
from flask_mail import Mail, Message
from app import app, db, mail
from app.models import Student
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
    if db.session.query(Student).filter_by(UserEmail=email).first() is not None:
        return jsonify(msg="That email is already in use."), 400

    student = Student(UserEmail=email, UserPass=generate_password_hash(password),
                      Created_on=datetime.datetime.utcnow(), hasConfirmedEmail=False)
    db.session.add(student)
    db.session.commit()
    return jsonify(id=student.UserID)


@app.route('/api/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    student = db.session.query(Student).filter_by(UserEmail=email).first()

    if student is None or not check_password_hash(student.UserPass, password):
        return jsonify(msg="Incorrect email or password."), 400

    access_token = create_access_token(identity=student.UserID)
    return jsonify(access_token=access_token)


@app.route('/api/auth/reset-pass-request', methods=['POST'])
def reset_pass_request():
    email = request.json.get('email')
    student = db.session.query(Student).filter_by(UserEmail=email).first()
    if student is not None:
        token_type = {"type": "resetPassword"}
        reset_email_token = create_access_token(identity=student.UserID, expires_delta=datetime.timedelta(hours=1), additional_claims=token_type)
        send_reset_pass_email(email, reset_email_token)

    # shows even if invalid email is entered to prevent checking if accounts exist
    return "A password reset link has been sent to " + email


@app.route('/api/auth/reset-pass', methods=['POST'])
@jwt_required()
def reset_pass():
    if get_jwt()['type'] != "resetPassword":
        return "Invalid token type", 403
    
    password = request.json.get('password')
    student = db.session.query(Student).get(get_jwt_identity())
    if student is not None:
        student.UserPass = generate_password_hash(password)
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
    student = db.session.query(Student).get(user_id)
    if student is None:
        return jsonify(msg="User with that ID does not exist."), 400

    return jsonify(userID=student.UserID, userEmail=student.UserEmail, createdOn=student.dateTime)
