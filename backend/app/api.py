from flask import jsonify, render_template
from app import app
from app.models import Student
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

@app.route('/model', methods=['GET'])
def get_model():
    print(Student(UserID=1, UserEmail="test", UserPass=123, dateTime=datetime.datetime.utcnow()))
    return "1"