# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    cs_core = []
    for i in range(8):
        cs_core.append(i)

    extra_courses = []
    for i in range(4):
        extra_courses.append(i)
    return render_template('index.html', cs_core=cs_core, extra_courses=extra_courses)

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', title="Favorites")

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', title='My Schedule')
    
@app.route('/color')
def color():
    neutral_colors = {
        "blackest": "navbars",
        "blacker": "cards, main ui elements",
        "black": "cards, ui elements",
        "darkest-gray": "cards, ui elements",
        "dark-gray": "extra color",
        "light-gray" : "extra color",
        "lightest-gray": "text, small ui elements",
        "white": "text",
        "whiter": "text",
        "whitest": "titles/high contrast text",
    }

    accent_colors = {
        "primary": "most buttons",
        "secondary": "important buttons, favorites",
        "warning": "deleting, errors, warnings",
        "confirm": "confirming, adding, success",
        "extra": "course badges, links",
    }

    return render_template('color_test.html', neutral_colors=neutral_colors, accent_colors=accent_colors)