# KSU Course Planner scraping script


#------------------------------------------------------------------------------
# modules

import requests # for http request 
from bs4 import BeautifulSoup   # for html parsing

# for db connection
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# database
from app import db
from app.models import Course, Degree


#------------------------------------------------------------------------------
# config

# get all data
def scrape():
    getAllPrograms()
    getCourses()
    

#------------------------------------------------------------------------------
# data retrieval

# courses

# gets all courses from ./coursesaz/seeall
def getCourses():
    coursesSite = getSiteData("http://catalog.kent.edu/coursesaz/seeall/")

    # get main text
    content = coursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = content.find_all('div', class_="courseblock")

    # get data for each course, get data
    for course in courses:
        getCourseData(course)


# gets all attributes for a course
# course = class "courseblock" inside html class "sc_sccoursedescs"
def getCourseData(course):
    # get all <p> tags
    attribute = course.find('p', class_="noindent")
    
    # CourseName, CourseID, CourseID_Type, CreditHours_Min, CreditHours_Max
    titleText = attribute.find('strong').text
    titleText = titleText.replace(u'\xa0', ' ') #&nbsp;
    titleText = titleText.split(' ')
    
    # CourseID, CourseID_Type
    CourseID = titleText[0] + ' ' + titleText[1]
    CourseID_Type = titleText[0]

    # CreditHours_Min, CreditHours_Max
    # get value(s)
    CreditHours = titleText[len(titleText)-3]
    # find upper and lower bounds
    CredMinandMax = CreditHours.split('-')
    if len(CredMinandMax) > 1:  # range
        CreditHours_Min = CredMinandMax[0]
        CreditHours_Max = CredMinandMax[1]
    else:   # not a range
        CreditHours_Min = CredMinandMax[0]
        CreditHours_Max = CredMinandMax[0]

    # CourseName
    CourseName = ""
    # add each relevant word in titleText to CourseName
    for word in range(2, len(titleText)-3): # cuz "3 Credit Hours"
        CourseName = CourseName + ' ' + titleText[word]
    CourseName = CourseName.strip()
    

    # description & prereqs
    attribute = attribute.find_next('p', class_="noindent")

    # get description text, eliminate other tags and &nbsp;
    descText = attribute.text
    attribute = attribute.find_next('p', class_="noindent")
    descText = descText[:descText.find(attribute.text)]
    descText = descText.replace(u'\xa0', ' ') #&nbsp;

    Prereqs = ""
    # find prereq in description, if exists (for edge case)
    lastIndex = descText.find(". Prerequisite: ")
    if lastIndex == -1:   # prereq is not inside description
        # description
        CourseDesc = descText.strip()
        
        # if prereq section exists
        if attribute.find('strong').text == "Prerequisite: ":   # prereqs exist
            attribute.find('strong').clear()
            Prereqs = attribute.text.strip()
            attribute = attribute.find_next('p', class_="noindent")
        
        else:   # prereqs not listed
            Prereqs = 'None.'

    else:   # prereq is inside description (edge case)
        # get description (first part)
        CourseDesc = descText[:lastIndex+1].strip()
        # then prereqs (last part)
        Prereqs = descText[lastIndex+len(". Prerequisite: "):].strip()

    # coreqs (edge case), go to next
    if attribute.find('strong').text == "Corequisite: ":
        attribute.find('strong').clear()
        # add coreqs to prereqs for simple inclusion
        Prereqs = Prereqs + ' Corequisites are ' + attribute.text.replace(u'\xa0', ' ').strip()
        attribute = attribute.find_next('p', class_="noindent")
    

    # course type (current attribute found in previous section)
    CourseType = ''
    # if Schedule Type attribute
    if attribute.find('strong').text == "Schedule Type: ":
        attribute.find('strong').clear()
        CourseType = attribute.text.replace(u'\xa0', ' ').strip()


    # contact hours (edge case needed: x lecture, y lab. see CS 10051)
    attribute = attribute.find_next('p', class_="noindent")
    ContactHours_Max = 0
    ContactHours_Min = 0
    # if Contact Hours attribute
    if attribute.find('strong').text == "Contact Hours: ":
        attribute.find('strong').clear()
        # get value(s)
        ContactHours = attribute.text.replace(u'\xa0', ' ').strip().split(' ')[0]
        # find upper and lower bounds
        ConMinandMax = ContactHours.split('-')
        if len(ConMinandMax) > 1:  # range
            ContactHours_Min = ConMinandMax[0]
            ContactHours_Max = ConMinandMax[1]
        else:   # not a range
            ContactHours_Min = ConMinandMax[0]
            ContactHours_Max = ConMinandMax[0]


    # grade type
    attribute = attribute.find_next('p', class_="noindent")
    GradeType = ''
    # if Grade Mode attribute
    if attribute.find('strong').text == "Grade Mode: ":
        attribute.find('strong').clear()
        GradeType = attribute.text.replace(u'\xa0', ' ').strip()


    # attributes (optional)
    Attributes = ''
    attribute = attribute.find_next('p', class_="noindent")
    # if Attributes attribute
    if attribute.find('strong').text == "Attributes: ":
        attribute.find('strong').clear()
        Attributes = attribute.text.replace(u'\xa0', ' ').strip()


    # insert into db
    addCourse(CourseID, CourseName, CourseDesc, CourseType,
        CreditHours_Min, CreditHours_Max, ContactHours_Min, ContactHours_Max,
        Prereqs, GradeType, CourseID_Type, Attributes)


# programs

# gets all programs from ./coursesaz
def getAllPrograms():
    # get program page data
    programsSite = getSiteData('http://catalog.kent.edu/coursesaz/')
    
    # find the meat of the page from #atozindex
    atozindex = programsSite.find(id="atozindex")

    # remove headers
    for header in atozindex.find_all(class_="letternav-head"):
        header.decompose()

    # find list of programs as <a> tags
    programList = atozindex.find_all('a')

    # get info for each degree
    for program in programList:
        # edge case: All Courses link
        if program.text != " All Kent State Courses":
            titleParts = program.text.split("(")

            # extract type and program name
            programType = titleParts[1][0:(len(titleParts[1].strip())-1)]
            programName = titleParts[0].strip()
            addProgram(programName, programType)


#------------------------------------------------------------------------------
# database insertion APIs

# adds course
# inputs vars are strings
def addCourse(CourseID, CourseName, CourseDesc, CourseType,
        CreditHours_Min, CreditHours_Max, ContactHours_Min, ContactHours_Max,
        Prereqs, GradeType, CourseID_Type, KentCore):
    insertRecord = True

    # see if record exists
    existing_course = db.session.query(Course).get([CourseID])
    
    # if so, check if it needs updated
    if existing_course:
        # construct search query
        matching_course = db.session.query(Course).filter_by(
            courseID = CourseID,
            courseName = CourseName,
            courseDesc = CourseDesc,
            courseType = CourseType,
            creditHoursMax = CreditHours_Max,
            creditHoursMin = CreditHours_Min,
            gradeType = GradeType,
            courseIDType = CourseID_Type,
            kentCore = KentCore,
            contactHoursMax = ContactHours_Max,
            contactHoursMin = ContactHours_Min,
            prereqs = Prereqs
        ).first()

        # check if found
        if matching_course: # dont do anything, call off insertion
            insertRecord = False
        else:   # difference found, needs updated, delete record
            db.session.delete(existing_course)
            db.session.commit()
    
    if insertRecord:    # if supposed to insert something
        # prep course object
        newCourse = Course(
            courseID = CourseID,
            courseName = CourseName,
            courseDesc = CourseDesc,
            courseType = CourseType,
            creditHoursMax = CreditHours_Max,
            creditHoursMin = CreditHours_Min,
            gradeType = GradeType,
            courseIDType = CourseID_Type,
            kentCore = KentCore,
            contactHoursMax = ContactHours_Max,
            contactHoursMin = ContactHours_Min,
            prereqs = Prereqs
        )
        
        # add and commit
        db.session.add(newCourse)
        db.session.commit()


# adds program
# input vars are strings
def addProgram(ProgramName, ProgramType):
    insertRecord = True

    # see if record exists
    existing_program = db.session.query(Degree).filter_by(
        degreeName = ProgramName,
        degreeType = ProgramType
    ).first()
    
    # if so, check if it needs updated
    if existing_program:
        # construct search query
        matching_program = db.session.query(Degree).filter_by(
            degreeName = ProgramName,
            degreeType = ProgramType
        ).first()

        # check if found
        if matching_program:    # dont do anything, call off insertion
            insertRecord = False
        else:   # difference found, needs updated, delete record
            db.session.delete(existing_program)
            db.session.commit()
    
    if insertRecord:    # if supposed to insert something
        # prep degree object
        newDegree = Degree(
            degreeName = ProgramName,
            degreeType = ProgramType
        )
        
        # add and commit
        db.session.add(newDegree)
        db.session.commit()


#------------------------------------------------------------------------------
# misc

# returns page as parsed html
# link = given page link as string
def getSiteData(link):
    response = requests.get(link)   # get page
    page = response.text # get html
    parsedPage = BeautifulSoup(page, 'html.parser')   # parse html
    return parsedPage


#------------------------------------------------------------------------------
# run the scraper

scrape()