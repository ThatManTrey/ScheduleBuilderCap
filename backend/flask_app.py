import os
from os.path import join, dirname
from dotenv import load_dotenv

# get environment config (internal file)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from app import app

if __name__ == '__main__':
    # use_reloader=False so code doesnt run twice
    app.run(use_reloader=False)
