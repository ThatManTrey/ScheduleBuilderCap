# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    cs_core = []
    for i in range(8):
        cs_core.append(i)

    cs_electives = []
    for i in range(4):
        cs_electives.append(i)
    return render_template('index.html', cs_core=cs_core, cs_electives=cs_electives)

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