from flask import jsonify
from app import app, db
from app.models import Course, User, FavCourse, Degree
from app.colors import *
from app.decorators import has_access_token, is_current_user

import datetime
from http import HTTPStatus

from sqlalchemy.sql import func


#------------------------------------------------------------------------------

#http://127.0.0.1:5000/ROUTE
#if post, do raw json in body


# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)


@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)

@app.route('/api/users/<int:user_id>', methods=['GET'])
@has_access_token()
@is_current_user
def get_user(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        return jsonify(msg="User with that ID does not exist."), HTTPStatus.BAD_REQUEST

    return jsonify(userID=user.userID, userEmail=user.userEmail, hasConfirmedEmail=user.hasConfirmedEmail, createdOn=user.createdOn)


#------------------------------------------------------------------------------
# university catalog

# courses

@app.route('/api/courses/<string:CourseType>', methods=['GET'])
def get_dept_courses(CourseType):
    courses = db.session.query(Course).filter_by(courseIDType = CourseType)
    arr_courses = []
    for course in courses:
        arr_courses.append(course.as_dict())
    return jsonify(deptCourses = arr_courses)

  
# use at your own risk, but works
@app.route('/api/courses/all', methods=['GET'])
#@has_api_key()
def get_all_courses():
    courses = db.session.query(Course).all()
    arr_courses = []
    for course in courses:
        arr_courses.append(course.as_dict())
    return jsonify(allCourses = arr_courses)


# degrees


@app.route('/api/degrees/all', methods=['GET'])
def get_all_degrees():
    the_degrees = db.session.query(Degree).all()
    arr_degrees = []
    for degree in the_degrees:
        arr_degrees.append(degree.as_dict())
    return jsonify(degrees = arr_degrees)


#------------------------------------------------------------------------------
# favorites

@app.route('/api/user/<int:user_id>/favorites', methods=['GET'])
# @has_access_token()
# @is_current_user
def get_favorite_courses(user_id):
    courses = db.session.query(FavCourse).filter_by(userID = user_id)
    arr_courses = []
    for course in courses:
        arr_courses.append(course.as_dict())
    return jsonify(favCourses = arr_courses)


@app.route('/api/user/<int:user_id>/favorites/<string:course_id>', methods=['POST'])
# @has_access_token()
# @is_current_user
def add_to_favorites(user_id, course_id):
    newFav = FavCourse(
            courseID = course_id,
            userID = user_id,
            dateTime = datetime.datetime.utcnow()   # get correct format
        )
    db.session.add(newFav)
    db.session.commit()


@app.route('/api/user/<int:user_id>/favorites/<string:course_id>', methods=['DELETE'])
# @has_access_token()
# @is_current_user
def remove_from_favorites(user_id, course_id):
    oldFav = db.session.query(FavCourse).filter_by(
            userID = user_id,
            courseID = course_id
        )
    db.session.delete(oldFav)
    db.session.commit()


#------------------------------------------------------------------------------
# ratings

# course

@app.route('/api/users/<int:user_id>/ratings', methods=['POST'])
# @has_access_token()
# @is_current_user
def add_rating(user_id):
    print()
    # if rating already exists
    #     return error
    # elif course doesnt exist
    #     return error
    # else:
    #     newRat = FavCourse(
    #             courseID = course_id,
    #             ratingQuality,
    #             ratingDifficulty
    #         )
    #     db.session.add(newRat)
    #     db.session.commit()


@app.route('/api/courses/<string:course_id>/ratings', methods=['GET'])
# @has_access_token()
# @is_current_user
def get_course_rating(course_id):
    the_ratings = db.session.query(Rating).filter_by(courseID = course_id)
    the_averages = db.session.query(
            func.avg(Rating.ratingQuality).label('quality'),
            func.avg(Rating.ratingDifficulty).label('difficulty')).filter_by(
                courseID = course_id
            )
    arr_ratings = []
    for rating in the_ratings:
        arr_ratings.append(rating.as_dict())
    dict_avg = the_averages.as_dict()
    return jsonify(ratings = arr_ratings, averages = dict_avg)


# user

@app.route('/api/users/<int:user_id>/ratings/<string:course_id> ', methods=['PUT'])
#or api/courses/<course_id>/ratings/<user_id>
# @has_access_token()
# @is_current_user
def edit_rating(user_id, course_id):
    print()


@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', methods=['DELETE'])
#or api/courses/<course_id>/ratings/<user_id>
# @has_access_token()
# @is_current_user
def remove_rating(user_id, course_id):
    print()


@app.route('/api/users/<int:user_id>/ratings', methods=['GET'])
# @has_access_token()
# @is_current_user
def get_user_ratings(user_id):
    print()
    # courses = db.session.query(Rating).filter_by(userID = user_id)
    # arr_courses = []
    # for course in courses:
    #     arr_courses.append(course.as_dict())
    # return jsonify(favCourses = arr_courses)
