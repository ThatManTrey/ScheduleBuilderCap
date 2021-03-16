from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import sshtunnel 

app = Flask(__name__)

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

#######################################################################################################      
#                       Set values for the student table and insert them                              #
#######################################################################################################
#newStudent = Student(UserID = '2',                                                                   #
#                    UserEmail = 'test2@gmail.com',                                                   #
#                    UserPass = 'plsworkagain',                                                       #
#                    dateTime = 'now+1...')                                                           #
#                                                                                                     #
#db.session.add(newStudent)                                                                           #
#db.session.commit()                                                                                  #
#######################################################################################################

#######################################################################################################      
#                       Run an SQL command... such as SELECT * FROM student                           #
#######################################################################################################
#UPDATING SOON
#######################################################################################################

	

	
