# A very simple Flask Hello World app for you to get started with...


#------------------------------------------------------------------------------
# imports

# flask
from flask import Flask, jsonify
from flask_cors import CORS

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import sshtunnel

# scraper
from scraperBot import start_scraper


#------------------------------------------------------------------------------
# scheduling

start_scraper()


#------------------------------------------------------------------------------
# app

app = Flask(__name__)


# db connect

if __name__ == '__main__':

    tunnel = sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'), ssh_username='KSUCoursePlanner', ssh_password='N5L3TR8mHq',
        remote_bind_address=('KSUCoursePlanner.mysql.pythonanywhere-services.com', 3306)
    )

    tunnel.start()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner:QMX4e6%nh!5[@127.0.0.1:{}/KSUCoursePlanner$test'.format(tunnel.local_bind_port)

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://KSUCoursePlanner.mysql.pythonanywhere-services.com'

db = SQLAlchemy(app)

# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

# db.commit()


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

neutral_colors = [
    {
        'name': 'blackest',
        'uses': 'navbars'
    },
    {
        'name': 'blacker',
        'uses': 'cards, main ui elements'
    },
    {
        'name': 'black',
        'uses': 'cards, ui elements'
    },
    {
        'name': 'darkest-gray',
        'uses': 'ui elements'
    },
    {
        'name': 'dark-gray',
        'uses': 'ui elements'
    },
    {
        'name': 'light-gray',
        'uses': 'extra color'
    },
    {
        'name': 'lightest-gray',
        'uses': 'text w/ less contrast'
    },
    {
        'name': 'white',
        'uses': 'text'
    },
    {
        'name': 'whiter',
        'uses': 'text'
    },
    {
        'name': 'whitest',
        'uses': 'titles/high contrast text'
    },
]

accent_colors = [
    {
        'name': 'primary',
        'uses': 'most buttons'
    },
    {
        'name': 'secondary',
        'uses': 'important buttons, favorites'
    },
    {
        'name': 'warning',
        'uses': 'deleting, errors, warnings'
    },
    {
        'name': 'confirm',
        'uses': 'confirming, adding, success'
    },
    {
        'name': 'extra',
        'uses': 'links'
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('test data')

# example api endpoints
# look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)

@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)


#------------------------------------------------------------------------------