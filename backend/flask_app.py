# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, render_template
from flask_cors import CORS

# points to the built files folder for Vue
app = Flask(__name__,
            template_folder="../frontend/dist/"
            )

CORS(app, resources={r'/*': {'origins': '*'}})

neutral_colors = [
    {
        'name': 'blackest',
        'uses': 'main ui elements'
    },
    {
        'name': 'blacker',
        'uses': 'ui elements'
    },
    {
        'name': 'black',
        'uses': 'ui elements'
    },
    {
        'name': 'darkest-gray',
        'uses': 'small ui elements'
    },
    {
        'name': 'dark-gray',
        'uses': 'extra color'
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
        'name': 'primary-dark',
        'uses': 'main accent color, somewhat important buttons'
    },
    {
        'name': 'primary-light',
        'uses': 'accent color for text/icons on dark background'
    },
    {
        'name': 'secondary',
        'uses': 'very important buttons, favorites'
    },
    {
        'name': 'warning-dark',
        'uses': 'deleting, errors, warnings (buttons/backgrounds)'
    },
    {
        'name': 'warning-light',
        'uses': 'deleting, errors, warnings (text/icons)'
    },
    {
        'name': 'confirm',
        'uses': 'confirming, add buttons/icons'
    },
    {
        'name': 'success',
        'uses': 'success message background'
    },
]

# Initial page rendering for PythonAnywhere
# renders index.html, static files are served by PythonAnywhere's
# web server (under the Web > static files tab)
# requires npm run build to be run in /frontend first

# if on pythonanywhere
if __name__ != '__main__':

    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

#
# API endpoints
#

# endpoint example, look at Theme.vue script for frontend example
@app.route('/api/colors/primary', methods=['GET'])
def get_primary_colors():
    return jsonify(neutral_colors)

@app.route('/api/colors/accent', methods=['GET'])
def get_accent_colors():
    return jsonify(accent_colors)


# run server only when local
if __name__ == '__main__':
    app.run()