from flask import jsonify
from app import app, db
from app.models import Course, User
from app.colors import *
from app.decorators import has_access_token, is_current_user, has_api_key

import datetime
from http import HTTPStatus

# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)

@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)

#http://127.0.0.1:5000/ROUTE
#if post, do raw json in body
@app.route('/api/courses/<string:CourseType>', methods=['GET'])
@has_api_key()
def get_dept_courses(CourseType):
    courses = db.session.query(Course).filter_by(courseIDType = CourseType)
    arr_courses = []
    for course in courses:
        arr_courses.append(course.as_dict())

    return jsonify(deptCourses = arr_courses)


@app.route('/api/users/<int:user_id>', methods=['GET'])
@has_api_key()
@has_access_token()
@is_current_user
def get_user(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        return jsonify(msg="User with that ID does not exist."), HTTPStatus.BAD_REQUEST

    return jsonify(userID=user.userID, userEmail=user.userEmail, hasConfirmedEmail=user.hasConfirmedEmail, createdOn=user.createdOn)
    

@app.route('/api/post-test', methods=['POST'])
@has_access_token()
def test_post():
    return ""

@app.route('/api/get-test', methods=['GET'])
@has_access_token()
def test_get():
    return ""