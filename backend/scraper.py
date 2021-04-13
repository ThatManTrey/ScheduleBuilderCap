# Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# APScheduler: https://apscheduler.readthedocs.io/en/stable/#
# $$$ means not tested

# todo: needs refactored to reduce coupling

#------------------------------------------------------------------------------
# modules

# scheduling
# from apscheduler.schedulers.background import BackgroundScheduler

# schedule helpers
# from time import sleep
# import atexit
# import datetime

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

# sets up schedule for scraper
# (won't work on pythonanywhere, doesnt support multithreading)
# def start_scraper():
#     # find next sunday date
#     today = datetime.date.today()
#     idx = 6-today.weekday()
#     sun = today + datetime.timedelta(idx)
    
#     scheduler = BackgroundScheduler()   # create new schedule for...
#     scheduler.add_job(
#         func=scrape,
#         trigger='date')  # ...now and...
#     scheduler.add_job(
#         func=scrape,
#         trigger='interval',
#         weeks=1,
#         start_date=sun)  # ...weekly on sunday
#     scheduler.start()
#     atexit.register(lambda: scheduler.shutdown())


# finds all data for db
def scrape():
    getAllPrograms()
    getCourses()
    

#------------------------------------------------------------------------------
# data retrieval

# COURSE STUFF

# gets all courses from coursesaz/seeall
def getCourses():
    coursesSite = getSiteData("http://catalog.kent.edu/coursesaz/seeall/")

    # get main text
    content = coursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = content.find_all('div', class_="courseblock")

    # get data for each course, 
    for course in courses:
        getCourseData(course)


# takes in html class "courseblock" inside html class "sc_sccoursedescs"
# http://catalog.kent.edu/coursesaz/aern/
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
    CreditHours = titleText[len(titleText)-3]
    CredMinandMax = CreditHours.split('-')
    if len(CredMinandMax) > 1:  # range
        CreditHours_Min = CredMinandMax[0]
        CreditHours_Max = CredMinandMax[1]
    else:   # not a range
        CreditHours_Min = CredMinandMax[0]
        CreditHours_Max = CredMinandMax[0]

    # CourseName
    CourseName = ""
    for word in range(2, len(titleText)-3): # cuz "3 Credit Hours"
        if word == 2:
            CourseName = CourseName + titleText[word]
        else:
            CourseName = CourseName + ' ' + titleText[word]
    

    # !description & prereqs
    attribute = attribute.find_next('p', class_="noindent")
    descText = attribute.text
    descText = descText.replace(u'\xa0', ' ') #&nbsp;
    Prereqs = ""

    # find prereq
    lastIndex = descText.find(". Prerequisite: ")
    if lastIndex == -1:   # prereq is in its own <p>
        # description
        CourseDesc = descText.strip()

        # prereqs
        attribute = attribute.find_next('p', class_="noindent")
        attribute.find('strong').clear()
        Prereqs = attribute.text.strip()

    else:   # prereq is inside description (edge case)
        CourseDesc = descText[:lastIndex+1].strip()
        Prereqs = descText[lastIndex+len(". Prerequisite: "):].strip()
    
    
    # course type
    attribute = attribute.find_next('p', class_="noindent")
    if attribute.find('strong').text == "Corequisite: ":
        attribute = attribute.find_next('p', class_="noindent")

    attribute.find('strong').clear()
    CourseType = attribute.text.replace(u'\xa0', ' ').strip()


    # !contact hours (edge case needed: x lecture, y lab. see CS 10051)
    attribute = attribute.find_next('p', class_="noindent")
    attribute.find('strong').clear()
    ContactHours = attribute.text.replace(u'\xa0', ' ').strip().split(' ')[0]
    ConMinandMax = ContactHours.split('-')
    if len(ConMinandMax) > 1:  # range
        ContactHours_Min = ConMinandMax[0]
        ContactHours_Max = ConMinandMax[1]
    else:   # not a range
        ContactHours_Min = ConMinandMax[0]
        ContactHours_Max = ConMinandMax[0]


    # grade type
    attribute = attribute.find_next('p', class_="noindent")
    attribute.find('strong').clear()
    GradeType = attribute.text.replace(u'\xa0', ' ').strip()


    # !attributes (optional)
    Attributes = None
    attribute = attribute.find_next('p', class_="noindent")
    if attribute.find('strong').text == "Attributes: ":
        attribute.find('strong').clear()
        Attributes = attribute.text.replace(u'\xa0', ' ').strip()


    # insert into db
    addCourse(CourseID, CourseName, CourseDesc, CourseType,
        CreditHours_Min, CreditHours_Max, ContactHours_Min, ContactHours_Max,
        Prereqs, GradeType, CourseID_Type, Attributes)


# PROGRAM STUFF

# gets all programs from coursesaz
def getAllPrograms():
    # get program page data
    programsSite = getSiteData('http://catalog.kent.edu/coursesaz/')
    
    # find the meat of the page #atozindex
    atozindex = programsSite.find(id="atozindex")

    # remove headers
    for header in atozindex.find_all(class_="letternav-head"):
        header.decompose()

    # find list of programs as <a> tags
    programList = atozindex.find_all('a')

    # get info for each degree
    for program in programList:
        if program.text != " All Kent State Courses":
            titleParts = program.text.split("(")

            # extract type and program name
            programType = titleParts[1][0:(len(titleParts[1].strip())-1)]
            programName = titleParts[0].strip()
            addProgram(programName, programType)


# DEGREE STUFF (still in development)

#$$$get all degrees, add each to database
def getAllDegrees():
    # get degree page data
    degreesSite = getSiteData('http://catalog.kent.edu/programsaz/')
    
    # find the meat of the page .az_sitemap
    az_sitemap = degreesSite.find(class_="az_sitemap")

    # find all lettered lists as <ul>
    letterList = az_sitemap.find_all('ul')
    letterList.remove(az_sitemap.find(class_="letternav"))
    
    # get lists of degrees as <a> tags
    # temporary version until future feature
    degreeList=[]
    for letter in letterList:
        for degree in letter.find_all('a'):
            degreeList.append(degree)

    # get info for each degree
    for degree in degreeList:
        # get site
        degreeCoursesSite = getSiteData("http://catalog.kent.edu" + degree.get('href') + "#programrequirementstext")

        # get code
        courselist = degreeCoursesSite.find(class_='sc_courselist')
        tbody = courselist.find('tbody')
        td = tbody.find(class_="odd")
        codecol = tbody.find(class_='codecol')

        # find type of first major course and degree name
        degreeType = codecol.find('a').text.split(u'\xa0')[0]
        degreeName = degree.text
        addDegree(degreeName, degreeType)

    # future feature
    # # open each program <a> tag to get courses from that dept
    # for degree in programList:
    #     getProgramConcentrations(program)


# $$$gets all degrees, add each to database
# given <a href="/colleges/COLLEGE/DEPT-SCHOOL/">PROGRAM_NAME</a>
def getDegreeConcentrations(degree):
    # get dept courses page data
    degreeCoursesSite = getSiteData('http://catalog.kent.edu' + degree.get('href') + "#roadmapstext")

    # get all course lists
    concLists = degreeCoursesSite.find_all('table', class_='sc_plangrid')

    # iterate through first list: major reqs
    for concentration in concLists:
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


# CORE STUFF

# $$$gets all core attributes, adds to courses
# http://catalog.kent.edu/undergraduate-university-requirements/
def getCore():
    coreSite = getSiteData("http://catalog.kent.edu/undergraduate-university-requirements/")

    # get main text
    content = coreSite.find(id='textcontainer')

    # get core lists
    coreLists = content.find_all('a')

    # get data for each list
    for coreList in coreLists:
        getCoreData(coreList.get('href').strip())


# $$$iterates through
# gets url of list
def getCoreData(url):
    # if not fye, parse site
    if url != "/undergraduate-university-requirements/destination-kent-state-first-year-experience/":
        parsedSite = getSiteData("http://catalog.kent.edu" + url)
    
    # diversity
    if url == "/undergraduate-university-requirements/diversity-course-requirement/":
        # domestic
        courseList = parsedSite.find(class_='sc_courselist')
        addCoreToCourses(courseList, "DIVD")

        # global
        courseList = courseList.find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "DIVG")

    # experiential
    elif url == "/undergraduate-university-requirements/experiential-learning-requirement/":
        courseList = parsedSite.find(class_='sc_courselist')
        addCoreToCourses(courseList, "ELR")

    # kent core
    elif url == "/undergraduate-university-requirements/kent-core/":
        # comp
        courseList = parsedSite.find(id="KCM").find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "KCMP")

        # math
        courseList = courseList.find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "KMCR")

        # humanities & fine arts
        courseList = courseList.find_next(class_='sc_courselist')
        # fine arts
        # find all headers
        for header in courseList.find_all(class_='areaheader'):
            # if fine arts header
            if header.find('span').text != "Fine Arts": # extract
                course = header
                lastCourse = header.find_next(class_="lastrow")
                while course != lastCourse: # while previous wasnt last row
                    # go to next, delete old course
                    oldCourse = course
                    course = course.find_next('tr')
                    oldCourse.decompose()
                    # add course
                    courseID = course.find(class_='codecol').find('a').text.replace(u'\xa0', ' ')
                    addCore(courseID, "KFA")
                course.decompose()
            else:   # delete the header
                header.decompose()
        # humanities
        addCoreToCourses(courseList, "KHUM")

        # social
        courseList = courseList.find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "KSS")

        # science
        courseList = courseList.find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "KBS")

        # additional
        courseList = courseList.find_next(class_='sc_courselist')
        addCoreToCourses(courseList, "KADL")

    # writing
    elif url == "/undergraduate-university-requirements/writing-intensive-course-requirement/":
        courseList = parsedSite.find(class_='sc_courselist')
        addCoreToCourses(courseList, "WIC")


# $$$adds core(s) to coreList courses
def addCoreToCourses(courseList, core):
    courses = courseList.find('tbody').find_all(class_='codecol')
    for course in courses:
        courseID = course.find('a').text.replace(u'\xa0', ' ')
        addCore(courseID, core)


#------------------------------------------------------------------------------
# database stuff

# adds course record
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

        # check results
        if matching_course: # dont do anything, call off insertion
            insertRecord = False
        else:   # difference found, needs updated, delete record
            db.session.delete(existing_course)
            db.session.commit()
    
    if insertRecord:    # if were supposed to insert something
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

        # check results
        if matching_program:    # dont do anything, call off insertion
            insertRecord = False
        else:   # difference found, needs updated, delete record
            db.session.delete(existing_program)
            db.session.commit()
    
    if insertRecord:    # if were supposed to insert something
        # prep degree object
        newDegree = Degree(
            degreeName = ProgramName,
            degreeType = ProgramType
        )
        
        # add and commit
        db.session.add(newDegree)
        db.session.commit()


# $$$adds degree listing (will be similar to addProgram)
def addDegree(DegreeName, DegreeType):
    print(DegreeName + " " + DegreeType)
    # # if record exists
    # if !(db.session.query(Degree).filter_by(
    #         degreeName = DegreeName,
    #         degreeType = DegreeType
    #     )):
    #     # prep course object
    #     newDegree = AllCourse(
    #             degreeName = DegreeName,
    #             degreeType = DegreeType
    #         )
        
    #     # add and commit
    #     db.session.add(newDegree)
    #     db.session.commit()


# $$$needs to get credit hours from courseID
def addProgramReq(DegreeID, CourseID, RequirementID, Paired):
    # change getProgramReqs if not
    print()


# $$$adds core
def addCore(CourseID, CoreAttr):
    print(CourseID, CoreAttr)


#------------------------------------------------------------------------------
# misc

# returns data as parsed html given link string
def getSiteData(link):
    response = requests.get(link)   # get page
    page = response.text # get html
    parsedPage = BeautifulSoup(page, 'html.parser').encode_contents(formatter='html')   # parse html
    return parsedPage


#------------------------------------------------------------------------------
# run it up

scrape()