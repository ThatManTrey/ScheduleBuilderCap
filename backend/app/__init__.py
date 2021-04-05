from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import DevelopmentConfig, ProductionConfig
import os

from http import HTTPStatus

# points to the built files folder for Vue
app = Flask(__name__, template_folder="../../frontend/dist/")

if os.environ['FLASK_ENV'] == "development":
    app.config.from_object(DevelopmentConfig)
else:
    import git
    app.config.from_object(ProductionConfig)


db = SQLAlchemy(app)


CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)
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

    # require API key for each request on pythonanywhere
    @app.before_request
    def before_request_func():   
        if request.endpoint == "index":
            return
            
        print(request.headers)
        # needed for github webhook defined below
        if "X-Hub-Signature-256" in request.headers:
            api_key = request.headers["X-Hub-Signature-256"]
        elif "Api-Key" in request.headers:
            api_key = request.headers["Api-Key"]
        else:
            return "API Key is required", HTTPStatus.BAD_REQUEST

        if api_key != app.config['SECRET_KEY']:
            return "Invalid API Key", HTTPStatus.BAD_REQUEST

    # for server updates
    @app.route('/update_server', methods=['POST'])
    def update_server():
        if request.method == 'POST':
            repo = git.Repo('/home/KSUCoursePlanner/ScheduleBuilderCap')
            origin = repo.remotes.origin

            origin.pull()

            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400


from app import auth, api
