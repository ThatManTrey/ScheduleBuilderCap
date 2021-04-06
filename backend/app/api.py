from flask import jsonify, request
from app import app, db
from app.models import Course, User, FavCourse, Degree, Rating
from app.colors import *
from app.decorators import has_access_token, is_current_user

import datetime
from http import HTTPStatus

from sqlalchemy.sql import func


# def get_that_json():
#     if "application/json" in request.headers["Content-Type"]:
#         return request.json
#     else:
#         return Response(status=415)


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


@app.route('/api/user/<int:user_id>/favorites/add', methods=['POST'])
# @has_access_token()
# @is_current_user
def add_to_favorites(user_id):
    body = request.get_json()
    
    # see if exists favorite or course exists
    favorite = db.session.query(FavCourse).get((body['course_id'], user_id))
    course = db.session.query(Course).get(body['course_id'])
    if favorite or not course:    # duplicate entry
        return jsonify(update = "fail")
    
    else:   # nonduplicate, update db
        newFav = FavCourse(
                courseID = body['course_id'],
                userID = user_id,
                dateTime = datetime.datetime.utcnow()   # get correct format
            )
        db.session.add(newFav)
        db.session.commit()
        return jsonify(update = "success")


@app.route('/api/user/<int:user_id>/favorites/remove', methods=['DELETE'])
# @has_access_token()
# @is_current_user
def remove_from_favorites(user_id):
    body = request.get_json()

    # find if record or course exists
    oldFav = db.session.query(FavCourse).get(
        {'userID': user_id, 'courseID': body['course_id']})
    course = db.session.query(Course).get(body['course_id'])
    if oldFav & course:  # exists
        db.session.delete(oldFav)
        db.session.commit()
        body = request.get_json()
        return jsonify(update = "success")
    
    else:   # some error, may not exist
        return jsonify(update = "fail")


#------------------------------------------------------------------------------
# ratings

# course

@app.route('/api/users/<int:user_id>/ratings', methods=['POST'])
# @has_access_token()
# @is_current_user
def add_rating(user_id):
    body = request.get_json()

    # see if course exists
    course = db.session.query(Course).get(body['course_id'])
    if course:  # course found, add rating
        newRat = Rating(
            courseID = body['course_id'],
            ratingQuality = body['quality'],
            ratingDifficulty = body['difficulty'],
            userID = user_id
        )
        db.session.add(newRat)
        db.session.commit()
        return jsonify(update = "success")
    
    else:   # error, course may not exist
        return jsonify(update = "fail")


@app.route('/api/courses/<string:course_id>/ratings', methods=['GET'])
# @has_access_token()
# @is_current_user
def get_course_rating(course_id):
    # notice float casting;
    # you cannot jsonify Decimal values from SQL
    # you CAN omit quotations in posted json for numbers

    # all ratings for course_id
    the_ratings = db.session.query(Rating).filter_by(courseID = course_id).all()
    arr_ratings = []
    for rating in the_ratings:
        entry = rating.as_dict()
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])
        arr_ratings.append(entry)
    print(arr_ratings)
    
    # averages for course_id
    the_averages = db.session.query(
                func.avg(Rating.ratingQuality).label('quality'),
                func.avg(Rating.ratingDifficulty).label('difficulty')
            ).filter_by(
                courseID = course_id
            ).first()
    quality = float(the_averages.quality)
    difficulty = float(the_averages.difficulty)
    
    
    return jsonify(
        ratings = arr_ratings,
        quality = quality,
        difficulty = difficulty
    )


# user

@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', methods=['PUT'])
#or api/courses/<course_id>/ratings/<user_id>
# @has_access_token()
# @is_current_user
def edit_rating(user_id, course_id):
    body = request.get_json()

    # see if rating exists
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()
    if rating:  # rating found, modify
        rating.ratingQuality = body['quality']
        rating.ratingDifficulty = body['difficulty']
        db.session.commit()
        return jsonify(update = "success")
    
    else:   # error, course may not exist
        return jsonify(update = "fail")


@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', methods=['DELETE'])
#or api/courses/<course_id>/ratings/<user_id>
# @has_access_token()
# @is_current_user
def remove_rating(user_id, course_id):
    # see if rating exists
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()
    if rating:  # rating found, delete rating
        db.session.delete(rating)
        db.session.commit()
        return jsonify(update = "success")
    
    else:   # error, rating may not exist
        return jsonify(update = "fail")


@app.route('/api/users/<int:user_id>/ratings', methods=['GET'])
# @has_access_token()
# @is_current_user
def get_user_ratings(user_id):
    ratings = db.session.query(Rating).filter_by(userID = user_id).all()
    arr_ratings = []
    for rating in ratings:
        entry = rating.as_dict()
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])
        arr_ratings.append(entry)
    return jsonify(ratedCourses = arr_ratings)


# #------------------------------------------------------------------------------
# # semesters


# @app.route('/api/users/<int:user_id>/semesters', methods=['GET'])
# # @has_access_token()
# # @is_current_user
# def get_semesters(user_id):
#     the_semesters = db.session.query(Semesters).filter_by(userID = user_id)
#     arr_semesters = []
#     for semester in the_semesters:
#         arr_courses.append(semester.as_dict())
#     return jsonify(semesters = arr_semesters)

# @app.route('/api/users/<int:user_id>/semesters', methods=['POST'])
# # @has_access_token()
# # @is_current_user
# def add_semester(semester_id, user_id, semester_name):
#     newSemester = Semester(
#             semesterID = semester_id,
#             userID = user_id,
#             semesterName = semester_name
#         )
#     db.session.add(newSemester)
#     db.session.commit()

# #I have absolutely no idea if this works... it should take the value of newName given in the function and change it in the db... it should... idk I hope it does...
# @app.route('/api/users/<int:user_id>/semesters/<string:semester_id>', methods=['PUT'])
# # @has_access_token()
# # @is_current_user
# def updateSemester(semesterID_given, newName):
#     new_name = session.query(Semesters).filter(Semesters.semesterID == semesterID_given).one()
#     new_name.semesterName = newName
#     db.session.commit()

# @app.route('/api/users/<int:user_id>/semesters/<string:semester_id>', methods=['DELETE'])
# # @has_access_token()
# # @is_current_user
# def remove_from_semesters(semester_id, user_id):
#     oldSemester = db.session.query(Semesters).filter_by(
#             semesterID = semester_id,
#             userID = user_id
#         )
#     db.session.delete(oldSemester)
#     db.session.commit()

# #------------------------------------------------------------------------------
# # semester courses

# @app.route('/api/users/<int:user_id>/semesters/<string:semester_id>/courses', methods=['GET'])
# # @has_access_token()
# # @is_current_user
# def get_semester_courses(semester_id):
#     the_semester_courses = db.session.query(SemesterCourses).filter_by(semesterID = semesterID)
#     arr_semester_courses = []
#     for semesterCourse in the_semester_courses:
#         arr_semester_courses.append(semesterCourse.as_dict())
#     return jsonify(semesterCourses = arr_semesters)

# @app.route('/api/users/<int:user_id>/semesters/<string:semester_id>/courses/<string:course_id>', methods=['POST'])
# # @has_access_token()
# # @is_current_user
# def add_semester_course(semester_id, course_id):
#     newSemesterCourse = Semester(
#             semesterID = semester_id,
#             courseID = course_id
#         )
#     db.session.add(newSemesterCourse)
#     db.session.commit()

# @app.route('/api/users/<int:user_id>/semesters/<string:semester_id>/courses/<string:course_id>', methods=['DELETE'])
# # @has_access_token()
# # @is_current_user
# def remove_from_semesters(semester_id, course_id):
#     oldSemesterCourse = db.session.query(SemesterCourses).filter_by(
#             semesterID = semester_id,
#             courseID = course_id
#         )
#     db.session.delete(oldSemesterCourse)
#     db.session.commit()
