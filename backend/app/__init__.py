from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import DevelopmentConfig, ProductionConfig
import os

from http import HTTPStatus
import git

# points to the built files folder for Vue
app = Flask(__name__, template_folder="../../frontend/dist/")

if os.environ['FLASK_ENV'] == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)


db = SQLAlchemy(app)

# from app import scraper
# #scraper.start_scraper()

CORS(app, resources={r'/*': {'origins': '*'}})
mail = Mail(app)
jwt = JWTManager(app)


if os.environ['FLASK_ENV'] == "production":
    # Initial page rendering needed for PythonAnywhere
    # requires npm run build to be run in /frontend first\
    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

    # not working, just put @has_api_key before each endpoint
    # require API key for each request on pythonanywhere
    # @app.before_request
    # def before_request_func():
    #     if "Api-Key" not in request.headers:
    #         return "API Key is required", HTTPStatus.BAD_REQUEST
    #     elif request.headers["Api-Key"] != app.config['SECRET_KEY']:
    #         return "Invalid API Key", HTTPStatus.BAD_REQUEST

    #     return ""

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
