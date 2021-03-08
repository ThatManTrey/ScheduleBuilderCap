# 

#------------------------------------------------------------------------------
# modules

# scheduler
from rq import Queue
from rq_scheduler import Scheduler

import requests # for http request 
from bs4 import BeautifulSoup   # for html parsing

from datetime import datetime

#------------------------------------------------------------------------------
# scraper setup and scheduling

# need to work on
def start_scraper():
    scheduler.schedule(
        scheduled_time=datetime.utcnow()+60,
        func=scrape,
        interval=86400  # once a day
    )
    scrape()


def scrape():
    #delete tables?
    
    getAllCourses()
    getAllPrograms()

#------------------------------------------------------------------------------
# data retrieval

# get all courses, add each to database
def getAllCourses():
    # get courses page data
    coursesSite = getSiteData('http://catalog.kent.edu/coursesaz/')
    
    #find the meat of the page #atozindex
    atozIndex = coursesSite.find(id="atozindex")

    # find all lettered lists as <ul>
    letterList = atozIndex.find_all('ul')
    
    # get lists of depts as <a> tags
    deptList=[]
    for letter in letterList:
        deptList.append(letter.find_all('a'))
    
    # open each dept <a> tag to get courses from that dept
    for dept in deptList:
        getdeptCourses(dept)


# gets all courses in dept page, adds each to database
# given <a href="/coursesaz/DEPT/">DEPT_NAME (ABBREVIATION)</a>
def getDeptCourses(dept):
    # get dept courses page data
    deptCoursesSite = getSiteData('http://catalog.kent.edu' + dept.get('href'))

    # get main text
    deptContent = deptCoursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = deptContent.find_all('div', class_="courseblock")

    # get data for each course, 
    for course in courses:
        getCourseData(course)


# NEED TO DO CORE PART
# takes in html class "courseblock" inside html class "sc_sccoursedescs"
# http://catalog.kent.edu/coursesaz/acct/
def getCourseData(course):
    # get all <p> tags
    attributes = course.find_all('p')
    
    # title (need to account for cores in name)
    # see http://catalog.kent.edu/coursesaz/hist/
    titleText = attributes[0].find('strong').get_text().split(" ")
    CourseID_Type = titleText[0]
    CourseID = CourseID_Type + " " + titleText[1]
    
    CourseName = ""
    for word in range(2, len(titleText)-3):
        CourseName = CourseName + word + " "
    
    # description (might need to account for '"'?)
    CourseDesc = attributes[1].get_text()
    firstPar = CourseDesc.find("(")
    secondPar = CourseDesc.find(")")
    for i in range(firstPar, secondPar+1)
        del CourseDesc[i]
    
    # course type (might need to account for '"'?)
    attributes[3].find('strong').clear()
    CourseType = attributes[3].get_text()

    # credit hours
    attributes[4].find('strong').clear()
    CreditHours = attributes[4].get_text()[0]

    # grade type
    attributes[5].find('strong').clear()
    GradeType = attributes[5].get_text()

    # insert into db
    addCourse(CourseID, CourseName, CourseDesc, CourseType, CreditHours, GradeType, CourseID_Type, KentCore)


# get all programs, add each to database
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
        getProgramConcentrations(program)


# I AM HERE gets all courses in dept page, adds each to database
# given <a href="/colleges/COLLEGE/DEPT-SCHOOL/">PROGRAM_NAME</a>
def getProgramConcentrations(program):
    # get dept courses page data
    programCoursesSite = getSiteData('http://catalog.kent.edu' + program.get('href') + "#programrequirementstext")

    # get main text
    deptContent = deptCoursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = deptContent.find_all('div', class_="courseblock")

    # get data for each concentration, 
    for course in courses:
        getCourseData(course)


#------------------------------------------------------------------------------
# database shit

# adds course record in db
def addCourse(CourseID, CourseName, CourseDesc, CourseType, CreditHours, GradeType, CourseID_Type, KentCore):
    

def addProgram():

#------------------------------------------------------------------------------
# misc

# returns data as parsed html given link string
def getSiteData(link):
    response = requests.get(link)   # get page
    page = response.text # get html
    parsedPage = BeautifulSoup(page, 'html.parser')   # parse html
    return parsedPage

#------------------------------------------------------------------------------
