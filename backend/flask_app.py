# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask import Flask 

# points to the built files folder for Vue
app = Flask(__name__,
            template_folder="../frontend/dist/"
            )

################################## DB CONNECTION #############################################
#pip install SQLAlchemy
#pip install mysqlclient
#pip install flask_sqlalchemy
#pip install sshtunnel
from flask_sqlalchemy import SQLAlchemy 
import sshtunnel 

#the connection stuff here through sshtunnel 
tunnel = sshtunnel.SSHTunnelForwarder(
('ssh.pythonanywhere.com'),
ssh_username='KSUCoursePlanner', ssh_password='N5L3TR8mHq',
remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
)

#starts the tunnel
tunnel.start()

#config to get in the main frame
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:QMX4e6%nh!5[@127.0.0.1:{}/KSUCoursePlanner$test'.format(tunnel.local_bind_port)

#set keyword db for basically everything (SQLAlchemy connection)
db = SQLAlchemy(app)

#Creates the "student" table... its in undercase not rly sure why... will fix later when not lazy.... 
class Student(db.Model):
    UserID = db.Column(db.Integer, primary_key=True) 
    UserEmail = db.Column(db.String(64))
    UserPass = db.Column(db.String(128))
    dateTime = db.Column(db.String(32))

#We need to declare these initializers so that we can actually insert values into them... without them we can not.
    def __init__(self, UserID, UserEmail, UserPass, dateTime):
#Setting everything equal to itself :)
        self.UserID = UserID
        self.UserEmail = UserEmail
        self.UserPass = UserPass
        self.dateTime = dateTime
	
class Semesters(db.Model):
    SemesterID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, primary_key=True)
    SemesterName = db.Column(db.String(64))

    def __init__(self, SemesterID, UserID, SemesterName):
        self.SemesterID = SemesterID
        self.UserID = UserID
        self.SemesterName = SemesteName


class Fav_Courses(db.Model):
    CourseID = db.Column(db.String(32), primary_key=True)
    UserID = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.String(32))

    def __init__(self, CourseID, UserID, dateTime):
        self.CourseID = CourseID
        self.UserID = UserID
        self.dateTime = dateTime
	
class Semester_Courses(db.Model):
    SemesterID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.String(32), primary_key=True)

    def __init__(self, SemesterID, CourseID):
        self.SemesterID = SemesterID
        self.CourseID = CourseID
        
class All_Courses(db.Model):
    CourseID = db.Column(db.String(32), primary_key=True)
    CourseName = db.Column(db.String(32))
    CourseDesc = db.Column(db.String(400))
    CourseType = db.Column(db.String(32))
    CreditHours = db.Column(db.String(32))
    GradeType = db.Column(db.String(24))
    CourseID_Type = db.Column(db.String(32))
    KentCore = db.Column(db.String(8))

    def __init__(self, CourseID, CourseName, CourseDesc, CourseType, CreditHours, GradeType, CourseID_Type, KentCore):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.CourseDesc = CourseDesc
        self.CourseType = CourseType
        self.CreditHours = CreditHours
        self.GradeType = GradeType
        self.CourseID_Type = CourseID_Type
        self.KentCore = KentCore
	
class Degree_Requirements(db.Model):
    DegreeID = db.Column(db.Integer, primary_key=True)
    RequirementID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.String(32), primary_key=True)
    Paired = db.Column(db.String(8))
    CreditHours = db.Column(db.String(32))

    def __init__(self, DegreeID, RequirementID, CourseID, Paired, CreditHours):
        self.DegreeID = DegreeID
        self.RequirementID = RequirementID
        self.CourseID = CourseID
        self.Paired = Paired
        self.CreditHours = CreditHours
	
class Other_Requirements(db.Model):
    Other_RequirementID = db.Column(db.Integer, primary_key=True)
    KentCore = db.Column(db.String(8), primary_key=True)
    CourseID = db.Column(db.String(32), primary_key=True)
    CreditHours = db.Column(db.String(32))

    def __init__(self, Other_RequirementID, KentCore, CourseID, CreditHours):
        self.Other_RequirementID = Other_RequirementID
        self.KentCore = KentCore
        self.CourseID = CourseID
        self.CreditHours = CreditHours
	
class Degree(db.Model):
    DegreeID = db.Column(db.Integer, primary_key=True)
    DegreeName = db.Column(db.String(32))	
    DegreeType = db.Column(db.String(16))

    def __init__(self, DegreeID, DegreeName, DegreeType):
        self.DegreeID = DegreeID
        self.DegreeName = DegreeName
        self.DegreeType = DegreeType
	
	
class Course_Attributes(db.Model):
    CourseID = db.Column(db.String(32), primary_key=True)
    AttributeID = db.Column(db.String(16), primary_key=True)

    def __init__(self, CourseID, AttributeID):
        self.CourseID = CourseID
        self.AttributeID = AttributeID
	
class Ratings(db.Model):
    RatingID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.String(32))
    RatingQuality = db.Column(db.Integer)
    RatingDifficulty = db.Column(db.Integer)

    def __init__(self, RatingID, CourseID, RatingQuality, RatingDifficulty):
        self.RatingID = RatingID
        self.CourseID = CourseID
        self.RatingQuality = RatingQuality
        self.RatingDifficulty = RatingDifficulty

##########################  DB END  ######################################################################## 

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

neutral_colors = [
    {
        'name': 'blackest',
        'uses': 'main ui elements'
    },
    {
        'name': 'blacker',
        'uses': 'ui elements'
    },
    {
        'name': 'black',
        'uses': 'ui elements'
    },
    {
        'name': 'darkest-gray',
        'uses': 'small ui elements'
    },
    {
        'name': 'dark-gray',
        'uses': 'extra color'
    },
    {
        'name': 'light-gray',
        'uses': 'extra color'
    },
    {
        'name': 'lightest-gray',
        'uses': 'text w/ less contrast'
    },
    {
        'name': 'white',
        'uses': 'text'
    },
    {
        'name': 'whiter',
        'uses': 'text'
    },
    {
        'name': 'whitest',
        'uses': 'titles/high contrast text'
    },
]

accent_colors = [
    {
        'name': 'primary-dark',
        'uses': 'main accent color, somewhat important buttons'
    },
    {
        'name': 'primary-light',
        'uses': 'accent color for text/icons on dark background'
    },
    {
        'name': 'secondary',
        'uses': 'very important buttons, favorites'
    },
    {
        'name': 'warning-dark',
        'uses': 'deleting, errors, warnings (buttons/backgrounds)'
    },
    {
        'name': 'warning-light',
        'uses': 'deleting, errors, warnings (text/icons)'
    },
    {
        'name': 'confirm',
        'uses': 'confirming, add buttons/icons'
    },
    {
        'name': 'success',
        'uses': 'success message background'
    },
]

# Initial page rendering for PythonAnywhere
# renders index.html, static files are served by PythonAnywhere's
# web server (under the Web > static files tab)
# requires npm run build to be run in /frontend first

# if on pythonanywhere
if __name__ != '__main__':

    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

#
# API endpoints
#

# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)

@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)


# run server only when local
if __name__ == '__main__':
    app.run()