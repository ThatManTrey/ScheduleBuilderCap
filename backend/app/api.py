from flask import jsonify, request
from app import app, db
from app.models import Course, User, FavCourse, Degree, Rating, Semester, SemesterCourse
from app.colors import *
from app.decorators import has_access_token, is_current_user

import datetime
from http import HTTPStatus

from sqlalchemy.sql import func

import enum


#------------------------------------------------------------------------------

# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)


@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)


@app.route('/api/users/<int:user_id>', endpoint='get_user', methods=['GET'])
@has_access_token()
@is_current_user()
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


@app.route('/api/courses/<int:page>/<int:per_page>', methods=['GET'])
def get_courses(page, per_page):
    # had to convert this to params because axios doesn't let you send 
    # a JSON body with get requests for some reason
    programs = request.args.get('programs').split(" ")
    keyword = request.args.get('keyword')
    sort_type = int(request.args.get('sortType'))
    is_ascending = request.args.get('isAscending') == "true"
    
    # find courses according to search parameter
    query = db.session.query(Course).filter(
        (Course.courseIDType.in_(programs)
        & (
            Course.courseID.like('%' + keyword + '%')
            | Course.courseDesc.like('%' + keyword + '%')
            | Course.courseName.like('%' + keyword + '%')
            | Course.prereqs.like('%' + keyword + '%')
        ))
    )

    # sort courses
    if sort_type == 1:   # courseId
        # gets length, location, courseID
        componentQuery = db.session.query(
            func.length(Course.courseID).label('length'),
            func.locate(" ", Course.courseID).label('loc'),
            Course.courseID
        ).subquery()

        # gets courseNo
        sortAttrQuery = db.session.query(
            func.substring(
                componentQuery.c.courseID,
                componentQuery.c.loc,
                componentQuery.c.length
            ).label('courseNo'),
            componentQuery.c.courseID.label('courseID')
        ).subquery()

        # joins original query with courseNo attribute
        query = query.outerjoin(
            sortAttrQuery,
            Course.courseID == sortAttrQuery.c.courseID
        )

        if is_ascending:
            query = query.order_by(sortAttrQuery.c.courseNo.asc())
        else:
            query = query.order_by(sortAttrQuery.c.courseNo.desc())

    elif sort_type == 2: # credits
        if is_ascending:
            query = query.order_by(Course.creditHoursMin.asc())
        else:
            query = query.order_by(Course.creditHoursMin.desc())

    elif sort_type == 3: # program
        if is_ascending:
            query = query.order_by(Course.courseIDType.asc())
        else:
            query = query.order_by(Course.courseIDType.desc())

    else:
        return jsonify(msg = "invalid sorting option"), HTTPStatus.BAD_REQUEST


    # retrieve results
    record_query = query.paginate(page, per_page, True)
    
    numResults = record_query.total
    numPages = record_query.pages
    results = record_query.items

    # # add page courses to results
    courses = []
    for result in results:
        courses.append(result.as_dict())

    return jsonify(
        coursesForPage = courses,
        numPages = numPages,
        numResults = numResults,
    )


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

@app.route( '/api/users/<int:user_id>/favorites', endpoint='get_favorites', methods=['GET'])
@has_access_token()
@is_current_user()
def get_favorites(user_id):
    # get courses and add favoritedOn
    courses = db.session.query(
        Course, FavCourse.favoritedOn
    ).join(
        FavCourse,
        Course.courseID == FavCourse.courseID
    ).filter(
        FavCourse.userID == user_id
    ).all()

    arr_courses = []
    for courseObj in courses:
        course = dict()
        course.update(courseObj[0].as_dict())
        course['favoritedOn'] = courseObj[1]
        arr_courses.append(course)
    return jsonify(favCourses = arr_courses)


@app.route('/api/users/<int:user_id>/favorites/<string:course_id>', endpoint='add_to_favorites', methods=['POST'])
@has_access_token()
@is_current_user()
def add_to_favorites(user_id, course_id):
    # see if exists favorite or course exists
    favorite = db.session.query(FavCourse).get((course_id, user_id))
    course = db.session.query(Course).get(course_id)
    
    # see if the user adding the course to their favorites has a real user_id, primary key is user_id + course_id
    real_user = db.session.query(User).get(user_id)
    
    # nonduplicate, update db
    if not favorite and course and real_user:
        newFav = FavCourse(
                courseID = course_id,
                userID = user_id,
                favoritedOn = datetime.datetime.utcnow()   # get correct format
            )
        db.session.add(newFav)
        db.session.commit()
        return jsonify()

    elif favorite:
        return jsonify(msg = "already favorited"), HTTPStatus.BAD_REQUEST
        
    elif not course:
        return jsonify(msg = "course not found"), HTTPStatus.BAD_REQUEST
    
    elif not real_user:
        return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/favorites/<string:course_id>', endpoint='remove_from_favorites', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_from_favorites(user_id, course_id):
    # find if record or course exists
    oldFav = db.session.query(
        FavCourse
    ).join(
        Course,
        Course.courseID == course_id
    ).filter(
        (FavCourse.userID == user_id)
        & (FavCourse.courseID == course_id)
    ).first()

    if oldFav:  # exists
        db.session.delete(oldFav)
        db.session.commit()
        return jsonify()
    
    return jsonify(msg = "favorite not found"), HTTPStatus.BAD_REQUEST


#------------------------------------------------------------------------------
# ratings

# course

@app.route('/api/users/<int:user_id>/ratings', endpoint='add_rating', methods=['POST'])
@has_access_token()
@is_current_user()
def add_rating(user_id):
    body = request.get_json()

    # see if course exists and if the user is a real user
    course = db.session.query(Course).get(body['course_id'])
    real_user = db.session.query(User).get(user_id)
    if course and real_user:  # course found, add rating
        newRat = Rating(
            courseID = body['course_id'],
            ratingQuality = body['quality'],
            ratingDifficulty = body['difficulty'],
            userID = user_id
        )
        db.session.add(newRat)
        db.session.commit()
        return jsonify()
    
    elif not real_user:
        return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST

    else:
        return jsonify(msg = "course not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/courses/<string:course_id>/ratings', endpoint='get_course_rating', methods=['GET'])
@has_access_token()
@is_current_user()
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
    
    if the_ratings:
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

    return jsonify(msg = "ratings not found")
    

# user

@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', endpoint='edit_rating', methods=['PUT'])
@has_access_token()
@is_current_user()
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
        return jsonify()
    
    return jsonify(msg = "rating not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', endpoint='ramove_rating', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_rating(user_id, course_id):
    # see if rating exists
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()

    if rating:  # rating found, delete rating
        db.session.delete(rating)
        db.session.commit()
        return jsonify()
    
    return jsonify(msg = "rating not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/ratings', endpoint='get_user_ratings', methods=['GET'])
@has_access_token()
@is_current_user()
def get_user_ratings(user_id):
    ratings = db.session.query(Rating).filter_by(userID = user_id).all()
    
    arr_ratings = []
    for rating in ratings:
        entry = rating.as_dict()
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])
        arr_ratings.append(entry)
    return jsonify(ratedCourses = arr_ratings)


#------------------------------------------------------------------------------
# semesters

@app.route('/api/users/<int:user_id>/semesters', endpoint='get_semesters', methods=['GET'])
@has_access_token()
@is_current_user()
def get_semesters(user_id):
    # get user semesters
    the_semesters = db.session.query(Semester).filter_by(
        userID = user_id
    ).all()

    # for each returned semester
    arr_semesters = []
    for semesterObj in the_semesters:
        # find semester courses
        the_courses = db.session.query(Course).join(
            SemesterCourse,
            SemesterCourse.courseID == Course.courseID
        ).filter(
            SemesterCourse.semesterID == semesterObj.semesterID
        ).all()

        # compile semester data
        semester = dict()
        semester['semesterName'] = semesterObj.semesterName
        semester['semesterId'] = semesterObj.semesterID
        semester['semesterCourses'] = []
        for course in the_courses:
            semester['semesterCourses'].append(course.as_dict())

        # add
        arr_semesters.append(semester)
    return jsonify(semesters = arr_semesters)


@app.route('/api/users/<int:user_id>/semesters', endpoint='add_semester', methods=['POST'])
@has_access_token()
@is_current_user()
def add_semester(user_id):
    body = request.get_json()

    # see if semester exists
    sem = db.session.query(Semester).filter_by(
        userID = user_id,
        semesterName = body['semester_name']
    ).first()

    real_user = db.session.query(User).get(user_id)
    if not sem and real_user: # create new semester
        newSemester = Semester(
            userID = user_id,
            semesterName = body['semester_name']
        )
        db.session.add(newSemester)
        db.session.commit()
        return jsonify()

    elif sem:
        return jsonify(msg = "semester already exists"), HTTPStatus.BAD_REQUEST

    else:
        return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>', endpoint='update_semester', methods=['PUT'])
@has_access_token()
@is_current_user()
def updateSemester(user_id, semester_id):
    body = request.get_json()

    # checks to see if the values exist 
    semester = db.session.query(Semester).get((semester_id, user_id))
    
    if semester:    # update name to semester_name
        semester.semesterName = body['semester_name']
        db.session.commit()
        return jsonify()

    return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>', endpoint='remove_semester', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_semester(user_id, semester_id):
    # checks to see if the values exist 
    oldSemester = db.session.query(Semester).get(
        {'userID': user_id, 'semesterID': semester_id})
    
    if oldSemester: # delete semester's courses & semester
        db.session.query(SemesterCourse).filter_by(
            semesterID = oldSemester.semesterID).delete()
        db.session.delete(oldSemester)
        db.session.commit()

        return jsonify()
    
    return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST


#------------------------------------------------------------------------------
# semester courses

@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>/courses', endpoint='get_semester_courses', methods=['GET'])
@has_access_token()
@is_current_user()
def get_semester_courses(user_id, semester_id):
    # find semester with user_id and semester_id, join with SemesterCourse
    the_semester_courses = db.session.query(Semester).filter_by(
        semesterID = semester_id,
        userID = user_id
        ).join(
            SemesterCourse, Semester.semesterID == SemesterCourse.semesterID
        ).all()       

    arr_semester_courses = []
    for semesterCourse in the_semester_courses:
        arr_semester_courses.append(semesterCourse.as_dict())
    return jsonify(semesterCourses = arr_semester_courses)


@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>/courses/<string:course_id>', endpoint='add_semester_course', methods=['POST'])
@has_access_token()
@is_current_user()
def add_semester_course(user_id, semester_id, course_id):
    # check if courseID and semesterID exist
    semester = db.session.query(Semester).get((semester_id, user_id))
    course = db.session.query(Course).get(course_id)
    
    if semester and course: # add semester course
        newSemesterCourse = SemesterCourse(
                semesterID = semester_id,
                courseID = course_id
            )
        db.session.add(newSemesterCourse)
        db.session.commit()
        return jsonify()
    
    elif not semester:
        return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST

    else:
        return jsonify(msg = "course does not exist"), HTTPStatus.BAD_REQUEST


@app.route('/api/users/<int:user_id>/semesters/<string:semester_id>/courses/<string:course_id>', endpoint='remove_from_semester', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_from_semester(user_id, semester_id, course_id):
    # check if semester course exists
    oldSemesterCourse = db.session.query(SemesterCourse).get(
        {'semesterID': semester_id, 'courseID': course_id})
    
    if oldSemesterCourse: # delete semester course
        db.session.delete(oldSemesterCourse)
        db.session.commit()
        return jsonify()
    
    return jsonify(msg = "semester course not found"), HTTPStatus.BAD_REQUEST