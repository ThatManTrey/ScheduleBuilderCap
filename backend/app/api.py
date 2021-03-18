from flask import jsonify
from app import app, db
from app.models import Student
from app.colors import *

import datetime

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
    