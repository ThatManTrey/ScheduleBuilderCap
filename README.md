# ScheduleBuilderCap

## Project Setup

### Backend

To run both Vue and Flask in dev you'll have to use two terminals. On the top bar In VSCode you can just do: Terminal > Split Terminal.

#### Flask

If you already have a venv and __pycache__ folder in the root directly, delete those then type these commands into one of the terminals:
```
$ cd backend
$ python -m venv venv
$ .\venv\Scripts\Activate
(venv)$ pip install -r packages.txt
(venv)$ flask run
``` 
Unlike Vue, Flask won't automatically update when you change a file, so you'll have to manually close and restart the server.

You can see whatever JSON data Flask is returning by typing in the api route directly, eg: http://localhost:5000/api/colors/primary

#### Database

put db setup info here

### Frontend (Vue.js)
From the project root, type in one of the terminals:
``` 
$ cd frontend
$ npm install
$ npm run serve
```

Then go to: http://localhost:8080/

This should be all you need to run Vue. If you're getting package errors, try manually deleting the node_modules and package_lock.json file and then try ```npm install``` again.

If you're getting a bunch of annoying warnings while running the app, they're usually formatting related and you can just do ```npm run lint``` to get rid of them. I think there's a way to have it automatically format Vue files whenever you save, but I haven't looked into it.

Test to make sure everythings working correctly by going to: http://localhost:8080/#/ping




