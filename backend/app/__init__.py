# put config/setup stuff here

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
#import sshtunnel


# points to the built files folder for Vue
app = Flask(__name__,
            template_folder="../frontend/dist/"
            )

# set keyword db for basically everything (SQLAlchemy connection)
db = SQLAlchemy(app)

# start scraper lol
from app import scraper
#scraper.start_scraper()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

from app import api