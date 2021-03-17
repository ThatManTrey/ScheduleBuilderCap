from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class AllCourse(Base):
    __tablename__ = 'all__courses'
    CourseID = Column(String(32), primary_key=True)
    CourseName = Column(String(32))
    CourseDesc = Column(String(400))
    CourseType = Column(String(32))
    CreditHours = Column(String(32))
    GradeType = Column(String(24))
    CourseID_Type = Column(String(32))
    KentCore = Column(String(8))
    

class CourseAttribute(Base):
    __tablename__ = 'course__attributes'

    CourseID = Column(String(32), primary_key=True, nullable=False)
    AttributeID = Column(String(16), primary_key=True, nullable=False)


class Degree(Base):
    __tablename__ = 'degree'

    DegreeID = Column(INTEGER(11), primary_key=True)
    DegreeName = Column(String(32))
    DegreeType = Column(String(16))


class DegreeRequirement(Base):
    __tablename__ = 'degree__requirements'

    DegreeID = Column(INTEGER(11), primary_key=True, nullable=False)
    RequirementID = Column(INTEGER(11), primary_key=True, nullable=False)
    CourseID = Column(String(32), primary_key=True, nullable=False)
    Paired = Column(String(8))
    CreditHours = Column(String(32))


class FavCourse(Base):
    __tablename__ = 'fav__courses'

    CourseID = Column(String(32), primary_key=True, nullable=False)
    UserID = Column(INTEGER(11), primary_key=True, nullable=False)
    dateTime = Column(String(32))


class OtherRequirement(Base):
    __tablename__ = 'other__requirements'

    Other_RequirementID = Column(INTEGER(11), primary_key=True, nullable=False)
    KentCore = Column(String(8), primary_key=True, nullable=False)
    CourseID = Column(String(32), primary_key=True, nullable=False)
    CreditHours = Column(String(32))


class Rating(Base):
    __tablename__ = 'ratings'

    RatingID = Column(INTEGER(11), primary_key=True)
    CourseID = Column(String(32))
    RatingQuality = Column(INTEGER(11))
    RatingDifficulty = Column(INTEGER(11))


class SemesterCourse(Base):
    __tablename__ = 'semester__courses'

    SemesterID = Column(INTEGER(11), primary_key=True, nullable=False)
    CourseID = Column(String(32), primary_key=True, nullable=False)


class Semester(Base):
    __tablename__ = 'semesters'

    SemesterID = Column(INTEGER(11), primary_key=True, nullable=False)
    UserID = Column(INTEGER(11), primary_key=True, nullable=False)
    SemesterName = Column(String(64))


class Student(Base):
    __tablename__ = 'student'

    UserID = Column(INTEGER(11), primary_key=True)
    UserEmail = Column(String(64))
    UserPass = Column(String(128))
    dateTime = Column(String(32))