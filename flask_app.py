# A very simple Flask Hello World app for you to get started with...

#------------------------------------------------------------------------------
# imports

# scraper
from scraper import start_scraper

# flask
from flask import Flask, jsonify
from flask_cors import CORS

#------------------------------------------------------------------------------
# scheduling
start_scraper()

#------------------------------------------------------------------------------
# routing

# A very simple Flask Hello World app for you to get started with...

app = Flask(__name__)

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