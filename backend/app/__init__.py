from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import DevelopmentConfig, ProductionConfig
from hmac import HMAC, compare_digest
from hashlib import sha256
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
    # requires npm run build to be run in /frontend first
    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

    def verify_signature(request):
        print("verifying signature....")
        received_signature = request.headers["X-Hub-Signature-256"].split("sha256=")[
            1]
        print("received signature: ", received_signature)
        if received_signature is None:
            return HTTPStatus.BAD_REQUEST

        key_as_bytes = bytes(app.config['SECRET_KEY'], 'utf-8')
        print("key as bytes: ", key_as_bytes)
        expected_signature = HMAC(
            key=key_as_bytes, msg=request.data, digestmod=sha256).hexdigest()
        print("expected signature: ", expected_signature)
        return compare_digest(received_signature, expected_signature)

    # require API key for each request on pythonanywhere

    @app.before_request
    def before_request_func():
        if request.endpoint == "index" or request.endpoint == "update_server":
            return

        api_key = request.headers["Api-Key"]
        if api_key is None:
            return "API Key is required", HTTPStatus.BAD_REQUEST

        if api_key != app.config['SECRET_KEY']:
            return "Invalid API Key", HTTPStatus.BAD_REQUEST

    # for server updates

    @app.route('/update_server', methods=['POST'])
    def update_server():
        if request.method == 'POST':
            if verify_signature(request):
                repo = git.Repo('/home/KSUCoursePlanner/ScheduleBuilderCap')
                origin = repo.remotes.origin

                origin.pull()
                print("if this is in the server log it should work")
                return 'Updated PythonAnywhere successfully'
            else:
                print("signature is not valid")
                return "Incorrect signature", HTTPStatus.FORBIDDEN
        else:
            return 'Wrong event type', HTTPStatus.BAD_REQUEST


from app import auth, api 