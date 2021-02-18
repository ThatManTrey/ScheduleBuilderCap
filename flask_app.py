# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    values = []
    for i in range(24):
        values.append(i)
    return render_template('index.html', values=values)

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