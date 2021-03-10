# A very simple Flask Hello World app for you to get started with...

import os
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__,
            template_folder="../frontend/dist/",
            static_folder="../frontend/dist/",
            )
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

#
# Initial page rendering for PythonAnywhere
# renders index.html and all the static files needed to start Vue
# requires npm run build to be run in /frontend first
#

# if on pythonanywhere
if __name__ != '__main__':

    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

    # @app.route('/js/<path:path>')
    # def send_js(path):
    #     return app.send_static_file(os.path.join('js', path).replace('\\', '/'))

    # @app.route('/css/<path:path>')
    # def send_css(path):
    #     return app.send_static_file(os.path.join('css', path).replace('\\', '/'))

    # @app.route('/img/<path:path>')
    # def send_img(path):
    #     return app.send_static_file(os.path.join('img', path).replace('\\', '/'))

    # @app.route('/fonts/<path:path>')
    # def send_fonts(path):
    #     return app.send_static_file(os.path.join('fonts', path).replace('\\', '/'))

    # @app.route('/favicon.ico')
    # def send_favicon():
    #     return app.send_static_file('favicon.ico')

#
# API endpoints
#

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

# run server when local
if __name__ == '__main__':
    app.run()