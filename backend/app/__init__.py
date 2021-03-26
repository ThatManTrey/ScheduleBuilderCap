from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager
import os
import git

# points to the built files folder for Vue
app = Flask(__name__, template_folder="../../frontend/dist/")
app.config["JWT_SECRET_KEY"] = os.urandom(32)

# set keyword db for basically everything (SQLAlchemy connection)
db = SQLAlchemy(app)

from app import scraper
#scraper.start_scraper()

CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Initial page rendering needed for PythonAnywhere
# requires npm run build to be run in /frontend first
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

# for server updates
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/KSUCoursePlanner/ScheduleBuilderCap')
        origin = repo.remotes.origin
    
        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


from app import auth, api
