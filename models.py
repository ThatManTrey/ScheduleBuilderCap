db = SQLAlchemy(app)

class Student(db.model):
	UserID = db.Column(db.Integer, primary_key=True)
	UserEmail = db.Column(db.String(64))
	UserPass = db.Column(db.String(128))
	dateTime = db.Column(db.String(32))
	
class Semesters(db.model):
	SemesterID = db.Column(db.Integer, primary_key=True)
	UserID = db.Column(db.Integer, primary_key=True)
	SemesterName = db.Column(db.String(64))

class Fav_Courses(db.model):
	CourseID = db.Column(db.String(32), primary_key=True)
	UserID = db.Column(db.Integer, primary_key=True)
	dateTime = db.Column(db.String(32))
	
class Semester_Courses(db.model):
	SemesterID = db.Column(db.Integer, primary_key=True)
	CourseID = db.Column(db.String(32), primary_key=True)
	
class All_Courses(db.model):
	CourseID = db.Column(db.String(32), primary_key=True)
	CourseName = db.Column(db.String(32))
	CourseDesc = db.Column(db.String(400))
	CourseType = db.Column(db.String(32))
	CreditHours = db.Column(db.String(32))
	GradeType = db.Column(db.String(24))
	CourseID_Type = db.Column(db.String(32))
	KentCore = db.Column(db.String(8))
	
class Degree_Requirements(db.model):
	DegreeID = db.Column(db.Integer, primary_key=True)
	RequirementID = db.Column(db.Integer, primary_key=True)
	CourseID = db.Column(db.String(32), primary_key=True)
	Paired = db.Column(db.String(8))
	CreditHours = db.Column(db.String(32))
	
class Other_Requirements(db.model):
	Other_RequirementID = db.Column(db.Integer, primary_key=True)
	KentCore = db.Column(db.String(8), primary_key=True)
	CourseID = db.Column(db.String(32), primary_key=True)
	CreditHours = db.Column(db.String(32))
	
class Degree(db.model):
	DegreeID = db.Column(db.Integer, primary_key=True)
	DegreeName = db.Column(db.String(32))	
	DegreeType = db.Column(db.String(16))
	
	
class Course_Attributes(db.model):
	CourseID = db.Column(db.String(32), primary_key=True)
	AttributeID = db.Column(db.String(16), primary_key=True)
	
class Ratings(db.model):
	RatingID = db.Column(db.Integer, primary_key=True)
	CourseID = db.Column(db.String(32))
	RatingQuality = db.Column(db.Integer)
	RatingDifficulty = db.Column(db.Integer)
	

	


	

	
