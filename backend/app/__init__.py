# put config/setup stuff here

from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import sshtunnel 
from flask_jwt_extended import JWTManager
import os

# points to the built files folder for Vue
app = Flask(__name__, template_folder="../frontend/dist/")

# disable annoying console warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# key to verify JWTs
# will invalidate existing tokens every time the server is restarted 
app.config["JWT_SECRET_KEY"] = os.urandom(32)

#the connection stuff here through sshtunnel 
tunnel = sshtunnel.SSHTunnelForwarder(
('ssh.pythonanywhere.com'),
ssh_username='KSUCoursePlanner', ssh_password='N5L3TR8mHq',
remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
)

#starts the tunnel
tunnel.start()

#config to get in the main frame
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:QMX4e6%nh!5[@127.0.0.1:{}/KSUCoursePlanner$test'.format(tunnel.local_bind_port)

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
