# web scraping demo for KSU Course Planner mk 2
# Trey Phillips, 2021

# beautifulsoup dox here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

import requests # for http request 
from bs4 import BeautifulSoup   # for html parsing

# CS2 (23001) would be found by going here (note protocol):
# 'http://catalog.kent.edu/search/?P=CS%2023001'

# How you find this...

# Step 1: go to roadmap
# 'http://catalog.kent.edu/colleges/as/cs/computer-science-bs/'
# get html
response = requests.get('http://catalog.kent.edu/colleges/as/cs/computer-science-bs/#programrequirementstext')
page = response.text
# parse html
parsedPage = BeautifulSoup(page, 'html.parser')

# Step 2: find table from list of tables/concentrations
tables = parsedPage.find_all('table', class_='sc_plangrid')
table = tables[0] # first table (nonconcentrated)

# Step 3: find list of courses
classes = []
for course in table.find_all('tr', class_='even'):
    classes.append(course)
for course in table.find_all('tr', class_='odd'):
    classes.append(course)

# Step 4: find course
courseLink = []
for course in classes:
    courseLink = course.find('a')
    if courseLink:
        code = courseLink.text
        code = code.replace("&nbsp;", "")
        print(code)
        if code == "CS 23001":
            print("this is the class!")
            break
        else:
           courseLink = []

# Step 5: go to class page
if courseLink:
    requests.get('http://catalog.kent.edu' + courseLink['href'])
else:
    print("not found")