from flask import jsonify, render_template
from app import app, db
from app.models import *
from app.colors import *
import datetime

# Initial page rendering needed for PythonAnywhere
# requires npm run build to be run in /frontend first
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)

@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)

@app.route('/query', methods=['GET'])
def get_model():
    student = db.session.query(Student).first()
    return jsonify(UserID=student.UserID, UserEmail=student.UserEmail)

#http://127.0.0.1:5000/ROUTE
#if post, do raw json in body
@app.route('/api/courses/<string:CourseType>', methods=['GET'])
def get_dept_courses(CourseType):
    courses = db.session.query(AllCourse).filter_by(CourseID_Type = CourseType)
    arr_courses = []
    for course in courses:
        arr_courses.append(course.as_dict())

    return jsonify(deptCourses = arr_courses)
    