import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# use_reloader=False so code doesnt run twice
from app import app

if __name__ == '__main__':
    app.run(use_reloader=False)
