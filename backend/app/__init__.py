from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import sshtunnel 

# points to the built files folder for Vue
app = Flask(__name__,
            template_folder="../frontend/dist/"
            )

db = SQLAlchemy(app)

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

#set keyword db for basically everything (SQLAlchemy connection)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

from app import api