
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
    getPrograms()

#------------------------------------------------------------------------------
# traversal functions

# get all courses, add each to database
def getAllCourses():
    # get courses page data
    coursesSite = getSiteData('http://catalog.kent.edu/coursesaz/')
    
    #find the meat of the page #atozindex
    atozIndex = coursesSite.find(id="atozindex")

    # find all lettered lists as <ul>
    letterList = deptList.find_all('ul')
    
    # get lists of depts as <a> tags
    deptList=[]
    for letter in letterList:
        deptList.append(letter.find_all('a'))
    
    # open each dept <a> tag to get courses fro that dept
    for dept in deptList:
        getdeptCourses(dept)


# gets all courses in dept page, adds each to database
# given <a href="/coursesaz/DEPT/">DEPT_NAME (ABBREVIATION)</a>
def getDeptCourses(dept):
    # get dept courses page data
    deptCoursesSite = getSiteData('http://catalog.kent.edu/' + dept.get('href'))

    # get main text
    deptContent = deptCoursesSite.find('div', class_="sc_sccoursedescs")

    # get courses list
    courses = deptContent.find_all('div', class_="courseblock")

    # get data for each course, 
    for course in courses:
        getCourseData(course)

# takes in html class "courseblock" inside html class "sc_sccoursedescs"
def getCourseData(course):
    ##################stopped here lol
    #http://catalog.kent.edu/coursesaz/acct/

def getPrograms():



def getProgramReqs():

#------------------------------------------------------------------------------
# database shit
def addCourse()

def addProgram() #?

#------------------------------------------------------------------------------
# misc

# returns data as parsed html given link string
def getSiteData(link):
    response = requests.get(link)   # get page
    page = response.text # get html
    parsedPage = BeautifulSoup(page, 'html.parser')   # parse html
    return parsedPage

#------------------------------------------------------------------------------
