from flask import jsonify, request
from app import app, db
from app.models import Student
import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


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

    student = Student(UserEmail=email, UserPass=generate_password_hash(
        password), dateTime=datetime.datetime.utcnow())
    db.session.add(student)
    db.session.commit()
    return jsonify(id=student.UserID)


@app.route('/api/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    student = db.session.query(Student).filter_by(UserEmail=email).first()
    is_correct_pass = check_password_hash(student.UserPass, password)
    if student is None or not is_correct_pass:
        return jsonify(msg="Incorrect email/password combination."), 400

    access_token = create_access_token(identity=student.UserID)
    return jsonify(access_token=access_token)

# protected resource
@app.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()     
@is_current_user
def get_user(user_id):
    student = db.session.query(Student).get(user_id)
    if student is None:
        return jsonify(msg="User with that ID does not exist."), 400

    return jsonify(userID=student.UserID, userEmail=student.UserEmail, createdOn=student.dateTime)