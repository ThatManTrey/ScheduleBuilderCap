# ScheduleBuilderCap

## Local Project Setup 

### Backend

To run both Vue and Flask in dev you'll have to use two terminals. On the top bar In VSCode you can just do: Terminal > Split Terminal.

#### Flask

If you already have a venv and __pycache__ folder in the root directly, delete those then type these commands into one of the terminals:
```
$ cd backend
$ python -m venv venv
$ .\venv\Scripts\Activate
(venv)$ pip install -r packages.txt
(venv)$ python flask_app.py
``` 
Unlike Vue, Flask won't automatically update when you change a file, so you'll have to manually close and restart the server.

Whenever you install a package with pip, remember to type 
``` pip freeze > packages.txt ```.

You can see whatever JSON data Flask is returning by typing in the api route directly, eg: http://localhost:5000/api/colors/primary

### Frontend (Vue.js)

Install Node.js first if you haven't yet.

From the project root, type in one of the terminals:
``` 
$ cd frontend
$ npm install
$ npm run serve
```

Then go to: http://localhost:8080/

## Deploying to PythonAnywhere

Open a bash console using "myvirtualenv" on PythonAnywhere (there should already be one running) and pull down the changes from whatever branch. Then type:

```
$ cd backend
$ pip install -r packages.txt
$ cd ../frontend
$ npm install
$ npm run build
```

Then go to the Web tab and reload the site.




