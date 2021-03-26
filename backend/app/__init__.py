from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager
import os

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

from app import auth, api
