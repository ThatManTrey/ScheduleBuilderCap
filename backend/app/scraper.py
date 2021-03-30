# Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# APScheduler: https://apscheduler.readthedocs.io/en/stable/#
# $$$ means not tested
# testing after fixing stuff

#------------------------------------------------------------------------------
# modules

# scheduling
from apscheduler.schedulers.background import BackgroundScheduler

# schedule helpers
import time
import atexit
import datetime

import requests # for http request 
from bs4 import BeautifulSoup   # for html parsing

# database
from app import db
from app.models import AllCourse

#------------------------------------------------------------------------------
# todo: scraper setup

# sets up schedule for scraper
def start_scraper():
    # find next sunday date
    today = datetime.date.today()
    idx = 6-today.weekday()
    sun = today + datetime.timedelta(idx)
    
    scheduler = BackgroundScheduler()   # create new schedule for...
    scheduler.add_job(
        func=scrape,
        trigger='date')  # ...now and...
    scheduler.add_job(
        func=scrape,
        trigger='interval',
        weeks=1,
        start_date=sun)  # ...weekly on sunday
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

# finds all data for db
def scrape():
    getCourses()
    getAllPrograms()
    

#------------------------------------------------------------------------------
# data retrieval

# COURSE STUFF

# gets all courses, adds each to db seeall
def getCourses():
    coursesSite = getSiteData('http://catalog.kent.edu/coursesaz/seeall/')

    # get main text
    content = coursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = content.find_all('div', class_="courseblock")

    # get data for each course, 
    for course in courses:
        getCourseData(course)


# takes in html class "courseblock" inside html class "sc_sccoursedescs"
# http://catalog.kent.edu/coursesaz/acct/
def getCourseData(course):
    # get all <p> tags
    attribute = course.find('p', class_="noindent")
    
    # CourseName, CourseID, CourseID_Type, CreditHours_Min, CreditHours_Max
    # CourseID, CourseID_Type
    titleText = attribute.find('strong').text.split(" ")
    CourseIDParts = titleText[0].split(u'\xa0')  #&nbsp;
    CourseID = CourseIDParts[0] + " " + CourseIDParts[1]
    CourseID_Type = CourseIDParts[0]
    # CreditHours_Min, CreditHours_Max
    CreditHours = titleText[len(titleText)-3]
    MinandMax = CreditHours.split('-')
    if len(MinandMax) > 1:  # range
        CreditHours_Min = MinandMax[0]
        CreditHours_Max = MinandMax[1]
    else:   # not a range
        CreditHours_Min = MinandMax[0]
        CreditHours_Max = MinandMax[0]
    # CourseName
    CourseName = ""
    for word in range(2, len(titleText)-3):
        CourseName = CourseName + titleText[word] + " "
    attribute = attribute.find_next('p', class_="noindent")
    
    # description
    CourseDesc = attribute.text
    lastIndex = CourseDesc.find("Prerequisite:") - 1
    CourseDesc = CourseDesc[1:lastIndex]
    
    # course type
    # use this while loop to get next attribute
    while attribute.find('strong').text != "Schedule Type: ":
        attribute = attribute.find_next('p', class_="noindent")
    attribute.find('strong').clear()
    CourseType = attribute.text

    # grade type
    while attribute.find('strong').text != "Grade Mode: ":
        attribute = attribute.find_next('p', class_="noindent")
    attribute.find('strong').clear()
    GradeType = attribute.text

    # insert into db
    addCourse(CourseID, CourseName, CourseDesc, CourseType, CreditHours_Min, CreditHours_Max, GradeType, CourseID_Type, None)


# PROGRAM STUFF (still in development)

# $$$get all programs, add each to database
def getAllPrograms():
    # get program page data
    programsSite = getSiteData('http://catalog.kent.edu/programsaz/')
    
    #find the meat of the page #az_sitemap
    az_sitemap = programsSite.find(id="az_sitemap")

    # find all lettered lists as <ul>
    letterList = az_sitemap.find_all('ul')
    
    # get lists of programs as <a> tags
    programList=[]
    for letter in letterList:
        programList.append(letter.find_all('a'))
    
    # open each program <a> tag to get courses from that dept
    for program in programList:
        getProgramDegrees(program)


# $$$gets all program degrees, add each to database
# given <a href="/colleges/COLLEGE/DEPT-SCHOOL/">PROGRAM_NAME</a>
def getProgramDegrees(program):
    # get dept courses page data
    programCoursesSite = getSiteData('http://catalog.kent.edu' + program.get('href') + "#roadmapstext")

    # get all course lists
    degreeLists = programCoursesSite.find_all('table', class_='sc_plangrid')

    # iterate through first list: major reqs
    for degree in degreeLists:
        # find header for degree
        DegreeName = degree.find_parent('h3').get_text()
        DegreeID = addProgram(DegreeName)

        # get the degree requirements biiiitch
        getDegreeReqs(degree, DegreeID)


# $$$gets all requirements for degree, add each to database
# given <table ... class="sc_plangrid">...</table>
# and DegreeID (from db)
def getDegreeReqs(degree, DegreeID):
    # find all tables rows, iterate through course table
    rows = degree.find_all('tr', class_='even') + degree.find_all('tr', class_='odd')
    RequirementID = 0
    for row in rows:
        # see if there is CourseID present
        codecol = row.find('td', class_='codecol')
        
        if codecol != "None":  # course code found
            #start RequirementID at 1, increment throughout
            RequirementID = RequirementID + 1
            
            # see if there are additional courses
            additionalCourses = codecol.find_all(class_='blockindent')
            
            if additionalCourses !="None":  # one course
                # add course to reqs
                CourseID = codecol.find('a', class_="code").get_text()
                addProgramReq(DegreeID, CourseID, RequirementID, None)
            
            else:   # multiple courses
                # add first course
                Paired = 1
                CourseID = codecol.find('a', class_="code").get_text()
                addProgramReq(DegreeID, CourseID, RequirementID, Paired)

                # iterate through req courses
                for course in additionalCourses:
                    if course.get_text()[0] == "&": # add to previous
                        CourseID = course.find('a', class_="code").get_text()
                        addProgramReq(DegreeID, CourseID, RequirementID, Paired)
                    elif course.get_text()[0:2] == "or": # add to previous
                        Paired = Paired + 1
                        CourseID = course.find('a', class_="code").get_text()
                        addProgramReq(DegreeID, CourseID, RequirementID, Paired)
        
        #else:   # not found
            # check if core or elective


# $$$CORE STUFF (havent started)
# http://catalog.kent.edu/undergraduate-university-requirements/kent-core/
def addCoreParts():
    print()


#------------------------------------------------------------------------------
# database shit

# adds course record in db
def addCourse(CourseID, CourseName, CourseDesc, CourseType, CreditHours_Min, CreditHours_Max, GradeType, CourseID_Type, KentCore):
    insertRecord = True
    
    # see if record exists
    existing_course = db.session.query(AllCourse).get([CourseID])
    
    # if so, check if it needs updated
    if existing_course:
        # construct search query
        existing_course = db.session.query(AllCourse).filter_by(
            CourseID = CourseID,
            CourseName = CourseName,
            CourseDesc = CourseDesc,
            CourseType = CourseType,
            CreditHours_Min = CreditHours_Min,
            CreditHours_Max = CreditHours_Max, 
            GradeType = GradeType,
            CourseID_Type = CourseID_Type,
            KentCore = KentCore
        ).first()

        # check results
        if existing_course: # difference found, needs updated, delete record
            db.session.delete(existing_course)
        else:   # dont do anything, call off insertion
            insertRecord = False
    
    if insertRecord:    # if were supposed to insert something
        # prep course object
        newCourse = AllCourse(
            CourseID = CourseID,
            CourseName = CourseName,
            CourseDesc = CourseDesc,
            CourseType = CourseType,
            CreditHours_Min = CreditHours_Min,
            CreditHours_Max = CreditHours_Max, 
            GradeType = GradeType,
            CourseID_Type = CourseID_Type,
            KentCore = KentCore
        )
        
        # add and commit
        db.session.add(newCourse)
        db.session.commit()

# $$$
def addProgram(DegreeName):
    print()
    DegreeID = int()
    return DegreeID

# $$$needs to get credit hours from courseID
def addProgramReq(DegreeID, CourseID, RequirementID, Paired):
    # change getProgramReqs if not
    print()


#------------------------------------------------------------------------------
# misc

# returns data as parsed html given link string
def getSiteData(link):
    response = requests.get(link)   # get page
    page = response.text # get html
    parsedPage = BeautifulSoup(page, 'html.parser')   # parse html
    return parsedPage


#------------------------------------------------------------------------------
