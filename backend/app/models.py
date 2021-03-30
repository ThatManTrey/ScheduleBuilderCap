from sqlalchemy import Column, DECIMAL, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Course(Base):
    __tablename__ = 'Courses'
    courseID = Column(String(32), primary_key=True)
    courseName = Column(text)
    courseDesc = Column(text)
    courseType = Column(String(32))
    creditHoursMax = Column(String(32))
    creditHoursMin = Column(String(32))
    gradeType = Column(String(24))
    courseIDType = Column(String(32))
    kentCore = Column(String(8))

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }


class Degree(Base):
    __tablename__ = 'Degrees'
    degreeID = Column(INTEGER(12), primary_key=True)
    degreeName = Column(String(32))
    degreeType = Column(String(16))

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }
    

class FavCourse(Base):
    __tablename__ = 'FavCourses'
    courseID = Column(String(32), primary_key=True, nullable=False)
    userID = Column(INTEGER(12), primary_key=True, nullable=False)
    favoritedOn = Column(DateTime)

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }

    
class Rating(Base):
    __tablename__ = 'Ratings'

    ratingID = Column(INTEGER(12), primary_key=True)
    courseID = Column(String(32))
    ratingQuality = Column(DECIMAL(4, 2))
    ratingDifficulty = Column(DECIMAL(4, 2))
    userID = Column(INTEGER(12), nullable=False)

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }


class SemesterCourse(Base):
    __tablename__ = 'SemesterCourses'

    semesterID = Column(INTEGER(12), primary_key=True, nullable=False)
    courseID = Column(String(32), primary_key=True, nullable=False)

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }


class Semester(Base):
    __tablename__ = 'Semesters'

    semesterID = Column(INTEGER(12), primary_key=True, nullable=False)
    userID = Column(INTEGER(12), primary_key=True, nullable=False)
    semesterName = Column(String(64))

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }


class User(Base):
    __tablename__ = 'Users'

    userID = Column(INTEGER(12), primary_key=True)
    userEmail = Column(String(64))
    userPass = Column(String(128))
    createdOn = Column(DateTime)
    hasConfirmedEmail = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }