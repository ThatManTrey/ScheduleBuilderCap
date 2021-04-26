# route APIs for frontend access to models


#------------------------------------------------------------------------------
# modules

from flask import jsonify, request
from app import app, db
from app.models import Course, User, FavCourse, Degree, Rating, Semester, SemesterCourse
from app.decorators import has_access_token, is_current_user

import datetime
from http import HTTPStatus

from sqlalchemy.sql import func


#------------------------------------------------------------------------------
# university catalog

# courses

# returns a list of courses
# uses pagination for ease in frontend use
# page = desired page
# per_page = max entries per page
# params:
#   programs is array of program abbreviation strings
#   keyword is search query
#   sortType{1=courseID, 2=credits, 3=programs}
#   isAscending is bool for sort order
@app.route('/api/courses/<int:page>/<int:per_page>', methods=['GET'])
def get_courses(page, per_page):
    # get search parameters from get request
    programs = request.args.get('programs').split(" ")
    keyword = request.args.get('keyword')
    sort_type = int(request.args.get('sortType'))
    is_ascending = request.args.get('isAscending') == "true"

    # create query

    # find courses according to search parameter
    if programs == ['']:    # no programs selected
        query = db.session.query(Course).filter(
            Course.courseID.like('%' + keyword + '%')
            | Course.courseDesc.like('%' + keyword + '%')
            | Course.courseName.like('%' + keyword + '%')
            | Course.prereqs.like('%' + keyword + '%')
        )

    else:   # programs selected
        query = db.session.query(Course).filter(
            (Course.courseIDType.in_(programs)
            & (
                Course.courseID.like('%' + keyword + '%')
                | Course.courseDesc.like('%' + keyword + '%')
                | Course.courseName.like('%' + keyword + '%')
                | Course.prereqs.like('%' + keyword + '%')
            ))
        )

    # modify query

    # sort courses
    if sort_type == 1:   # by courseId
        # gets length, location, courseID
        componentQuery = db.session.query(
            func.length(Course.courseID).label('length'),
            func.locate(" ", Course.courseID).label('loc'),
            Course.courseID
        ).subquery()

        # gets courseNo from courseID
        sortAttrQuery = db.session.query(
            func.substring(
                componentQuery.c.courseID,
                componentQuery.c.loc,
                componentQuery.c.length
            ).label('courseNo'),
            componentQuery.c.courseID.label('courseID')
        ).subquery()

        # join original query with courseNo attribute
        query = query.outerjoin(
            sortAttrQuery,
            Course.courseID == sortAttrQuery.c.courseID
        )

        # sort order
        if is_ascending:
            query = query.order_by(sortAttrQuery.c.courseNo.asc())
        else:
            query = query.order_by(sortAttrQuery.c.courseNo.desc())

    elif sort_type == 2: # by credits
        # sort order
        if is_ascending:
            query = query.order_by(Course.creditHoursMin.asc())
        else:
            query = query.order_by(Course.creditHoursMin.desc())

    elif sort_type == 3: # by program
        # sort order
        if is_ascending:
            query = query.order_by(Course.courseIDType.asc())
        else:
            query = query.order_by(Course.courseIDType.desc())

    else:   # invalid choice
        return jsonify(msg = "invalid sorting option"), HTTPStatus.BAD_REQUEST


    # execute query
    record_query = query.paginate(page, per_page, True)
    
    # get results and pagination attributes
    numResults = record_query.total
    numPages = record_query.pages
    results = record_query.items

    # # add results to course array
    courses = []
    for result in results:
        courses.append(result.as_dict())

    return jsonify(
        coursesForPage = courses,
        numPages = numPages,
        numResults = numResults,
    )


# degrees

# returns a list of all courses
@app.route('/api/degrees/all', methods=['GET'])
def get_all_degrees():
    the_degrees = db.session.query(Degree).all()

    # add degrees to array
    arr_degrees = []
    for degree in the_degrees:
        arr_degrees.append(degree.as_dict())

    return jsonify(degrees = arr_degrees)
    

#------------------------------------------------------------------------------
# favorites

# returns a users favorites
# user_id = the unique id for a user
@app.route( '/api/users/<int:user_id>/favorites', endpoint='get_favorites', methods=['GET'])
@has_access_token()
@is_current_user()
def get_favorites(user_id):
    # get courses w/ favoritedOn attributes
    courses = db.session.query(
        Course, FavCourse.favoritedOn
    ).join(
        FavCourse,
        Course.courseID == FavCourse.courseID
    ).filter(
        FavCourse.userID == user_id
    ).all()

    # add courses to array
    arr_courses = []
    for courseObj in courses:
        # prepare object as dictionary
        course = dict()
        # add main course attributes
        course.update(courseObj[0].as_dict())
        # add favoritedOn attribute
        course['favoritedOn'] = courseObj[1]

        arr_courses.append(course)

    return jsonify(favCourses = arr_courses)


# adds course to user favorites
# user_id = the unique id for a user
# course_id = course identifier
@app.route('/api/users/<int:user_id>/favorites/<string:course_id>', endpoint='add_to_favorites', methods=['POST'])
@has_access_token()
@is_current_user()
def add_to_favorites(user_id, course_id):
    # see if favorite or course exists
    favorite = db.session.query(FavCourse).get((course_id, user_id))
    course = db.session.query(Course).get(course_id)
    
    # see if the user adding the course to their favorites is real
    real_user = db.session.query(User).get(user_id)
    
    if not favorite and course and real_user:   # nonduplicate, update db
        newFav = FavCourse(
                courseID = course_id,
                userID = user_id,
                favoritedOn = datetime.datetime.utcnow()   # get correct format
            )
        db.session.add(newFav)
        db.session.commit()
        return jsonify()

    elif favorite:  # already favorited
        return jsonify(msg = "already favorited"), HTTPStatus.BAD_REQUEST
        
    elif not course:    # course not found
        return jsonify(msg = "course not found"), HTTPStatus.BAD_REQUEST
    
    elif not real_user: # user not found
        return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST


# removes course to user favorites
# user_id = the unique id for a user
# course_id = course identifier
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

    if oldFav:  # favorite exists, delete
        db.session.delete(oldFav)
        db.session.commit()
        return jsonify()
    
    # favorite not found
    return jsonify(msg = "favorite not found"), HTTPStatus.BAD_REQUEST


#------------------------------------------------------------------------------
# ratings

# course

# adds rating for course from user
# user_id = the unique id for a user
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
    
    elif not real_user: # user not found
        return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST

    else:   # course not found
        return jsonify(msg = "course not found"), HTTPStatus.BAD_REQUEST


# returns ratings and average ratings for course
# course_id = course identifier
@app.route('/api/courses/<string:course_id>/ratings', endpoint='get_course_rating', methods=['GET'])
def get_course_rating(course_id):
    # all ratings for course_id
    the_ratings = db.session.query(Rating).filter_by(courseID = course_id).all()
    
    # add ratings to array
    arr_ratings = []
    for rating in the_ratings:
        entry = rating.as_dict()

        # cast from Decimal to float for jsonify compatibility
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])

        arr_ratings.append(entry)
    
    # see if ratings exist
    if the_ratings: # ratings found
        # averages for course_id
        the_averages = db.session.query(
                    func.avg(Rating.ratingQuality).label('quality'),
                    func.avg(Rating.ratingDifficulty).label('difficulty')
                ).filter_by(
                    courseID = course_id
                ).first()

        # cast from Decimal to float for jsonify compatibility
        quality = float(the_averages.quality)
        difficulty = float(the_averages.difficulty)

        return jsonify(
            ratings = arr_ratings,
            quality = quality,
            difficulty = difficulty
        )

    # ratings not found
    return jsonify(msg = "ratings not found")
    

# user

# edits a user's rating
# user_id = the unique id for a user
# course_id = course identifier
@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', endpoint='edit_rating', methods=['PUT'])
@has_access_token()
@is_current_user()
def edit_rating(user_id, course_id):
    body = request.get_json()

    # find rating
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()

    # see if rating exists
    if rating:  # rating found, modify it
        rating.ratingQuality = body['quality']
        rating.ratingDifficulty = body['difficulty']
        db.session.commit()
        return jsonify()
    
    # rating not found
    return jsonify(msg = "rating not found"), HTTPStatus.BAD_REQUEST


# removes a user's rating
# user_id = the unique id for a user
# course_id = course identifier
@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', endpoint='ramove_rating', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_rating(user_id, course_id):
    # find rating
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()

    # see if rating exists
    if rating:  # rating found, delete it
        db.session.delete(rating)
        db.session.commit()
        return jsonify()
    
    # rating not found
    return jsonify(msg = "rating not found"), HTTPStatus.BAD_REQUEST


# returns ratings for user
# user_id = the unique id for a user
@app.route('/api/users/<int:user_id>/ratings', endpoint='get_user_ratings', methods=['GET'])
@has_access_token()
@is_current_user()
def get_user_ratings(user_id):
    # all ratings for user id
    ratings = db.session.query(Rating).filter_by(userID = user_id).all()
    
    # add ratings to array
    arr_ratings = []
    for rating in ratings:
        entry = rating.as_dict()

        # cast from Decimal to float for jsonify compatibility
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])

        arr_ratings.append(entry)
    
    return jsonify(ratedCourses = arr_ratings)


# return course rating for user
# user_id = the unique id for a user
# course_id = course identifier
@app.route('/api/users/<int:user_id>/ratings/<string:course_id>', endpoint='get_user_course_rating', methods=['GET'])
@has_access_token()
@is_current_user()
def get_user_course_rating(user_id, course_id):
    # find rating
    rating = db.session.query(Rating).filter_by(
        courseID = course_id,
        userID = user_id
    ).first()

    #arr_ratings = []
    # see if rating exists
    if rating:  # rating found
        entry = rating.as_dict()

        # cast from Decimal to float for jsonify compatibility
        entry['ratingQuality'] = float(entry['ratingQuality'])
        entry['ratingDifficulty'] = float(entry['ratingDifficulty'])

        #arr_ratings.append(entry)

        return jsonify(rating = entry)

    return jsonify(msg = "rating not found"), HTTPStatus.BAD_REQUEST


#------------------------------------------------------------------------------
# semesters

# returns semesters for user
# user_id = the unique id for a user
@app.route('/api/users/<int:user_id>/semesters', endpoint='get_semesters', methods=['GET'])
@has_access_token()
@is_current_user()
def get_semesters(user_id):
    # get user semesters
    the_semesters = db.session.query(Semester).filter_by(
        userID = user_id
    ).all()
    
    arr_semesters = []
    # add each semester to array
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
        # add courses to semester
        for course in the_courses:
            semester['semesterCourses'].append(course.as_dict())

        # add
        arr_semesters.append(semester)

    return jsonify(semesters = arr_semesters)


# adds semester for user
# user_id = the unique id for a user
@app.route('/api/users/<int:user_id>/semesters', endpoint='add_semester', methods=['POST'])
@has_access_token()
@is_current_user()
def add_semester(user_id):
    body = request.get_json()

    # find user
    real_user = db.session.query(User).get(user_id)

    # see if user exists
    if real_user: # user found, create new semester
        newSemester = Semester(
            userID = user_id,
            semesterName = body['semester_name']
        )
        db.session.add(newSemester)
        db.session.commit()
        return jsonify()

    # user not found
    return jsonify(msg = "user not found"), HTTPStatus.BAD_REQUEST


# changes semester name for user
# user_id = the unique id for a user
# semester_id = semester identifier
@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>', endpoint='update_semester', methods=['PUT'])
@has_access_token()
@is_current_user()
def updateSemester(user_id, semester_id):
    body = request.get_json()

    # find semester
    semester = db.session.query(Semester).get((semester_id, user_id))
    
    # see if semester exists
    if semester:    # semester found, update name to semester_name
        semester.semesterName = body['semester_name']
        db.session.commit()
        return jsonify()

    # semester not found
    return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST


# removes semester for user
# user_id = the unique id for a user
# semester_id = semester identifier
@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>', endpoint='remove_semester', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_semester(user_id, semester_id):
    # find semester
    oldSemester = db.session.query(Semester).get(
        {'userID': user_id, 'semesterID': semester_id})
    
    # see if semester exists
    if oldSemester: # semester found, delete semester and its courses
        db.session.query(SemesterCourse).filter_by(
            semesterID = oldSemester.semesterID).delete()
        db.session.delete(oldSemester)
        db.session.commit()

        return jsonify()
    
    # semester not found
    return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST


#------------------------------------------------------------------------------
# semester courses

# returns courses for user semester
# user_id = the unique id for a user
# semester_id = semester identifier
@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>/courses', endpoint='get_semester_courses', methods=['GET'])
@has_access_token()
@is_current_user()
def get_semester_courses(user_id, semester_id):
    # find courses for semester
    the_semester_courses = db.session.query(Semester).filter_by(
        semesterID = semester_id,
        userID = user_id
        ).join(
            SemesterCourse, Semester.semesterID == SemesterCourse.semesterID
        ).all()       

    arr_semester_courses = []
    # add each course to array
    for semesterCourse in the_semester_courses:
        arr_semester_courses.append(semesterCourse.as_dict())

    return jsonify(semesterCourses = arr_semester_courses)


# adds semester course to user semester
# user_id = the unique id for a user
# semester_id = semester identifier
# course_id = course identifier
@app.route('/api/users/<int:user_id>/semesters/<int:semester_id>/courses/<string:course_id>', endpoint='add_semester_course', methods=['POST'])
@has_access_token()
@is_current_user()
def add_semester_course(user_id, semester_id, course_id):
    # find course and semester
    semester = db.session.query(Semester).get((semester_id, user_id))
    course = db.session.query(Course).get(course_id)
    
    # see if course and semester exist
    if semester and course: # both found, add semester course
        newSemesterCourse = SemesterCourse(
                semesterID = semester_id,
                courseID = course_id
            )
        db.session.add(newSemesterCourse)
        db.session.commit()
        return jsonify()
    
    # semester not found
    elif not semester:
        return jsonify(msg = "semester not found"), HTTPStatus.BAD_REQUEST

    # course does not exist
    else:
        return jsonify(msg = "course does not exist"), HTTPStatus.BAD_REQUEST


# removes semester course from user semester
# user_id = the unique id for a user
# semester_id = semester identifier
# course_id = course identifier
@app.route('/api/users/<int:user_id>/semesters/<string:semester_id>/courses/<string:course_id>', endpoint='remove_from_semester', methods=['DELETE'])
@has_access_token()
@is_current_user()
def remove_from_semester(user_id, semester_id, course_id):
    # find semester course
    oldSemesterCourse = db.session.query(SemesterCourse).get(
        {'semesterID': semester_id, 'courseID': course_id})
    
    # see if semester course exists
    if oldSemesterCourse: # semester course found, delete
        db.session.delete(oldSemesterCourse)
        db.session.commit()
        return jsonify()
    
    # semester course not found
    return jsonify(msg = "semester course not found"), HTTPStatus.BAD_REQUEST