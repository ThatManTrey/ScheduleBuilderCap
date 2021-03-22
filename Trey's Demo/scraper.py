#web scraping demo for KSU Course Planner
#Trey Phillips, 2021

#splinter docs here: https://splinter.readthedocs.io/en/latest/
#using flask: https://splinter.readthedocs.io/en/latest/drivers/flask.html

#chrome webdriver: https://chromedriver.chromium.org/
#edge webdriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
#firefox webdriver: https://github.com/mozilla/geckodriver/releases

from splinter import Browser
import time

#must find driver for your pc. can specify browser. default is firefox
browser = Browser()

print("CS2 (23001) would be found by going here (note protocol):")
print("http://catalog.kent.edu/search/?P=CS%2023001")
browser.visit('http://catalog.kent.edu/search/?P=CS%2023001')

print("How you find this...")

print("Step 1: go to roadmap")
browser.visit('http://catalog.kent.edu/colleges/as/cs/computer-science-bs/#NCC')
time.sleep(5)

print("Step 2: find table (this will return list of tables if concentrations exist)")
tables = browser.find_by_css(".sc_plangrid")
table = tables[0].find_by_tag('tbody')
time.sleep(5)

print("Step 3: find list of courses")
classes = []
for course in table.find_by_css('.even'):
    classes.append(course)
for course in table.find_by_css('.odd'):
    classes.append(course)
time.sleep(5)

print("Step 4: find course")
courseLink = []
for course in classes:
    courseLink = course.find_by_tag('a')
    if courseLink:
        code = courseLink.value
        print(code)
        if code == "CS 23001":
            print("this is the class!")
            break
        else:
            print("this isn't the class")
            courseLink = []
time.sleep(5)

print("Step 5: go to class page")
if courseLink:
    courseLink.click()
else:
    print("not found")
input()

browser.quit()