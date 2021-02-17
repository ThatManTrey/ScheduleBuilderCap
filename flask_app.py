# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/login')
def login():
    return render_template('login.html')

