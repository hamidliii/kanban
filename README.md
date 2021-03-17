# Welcome to Simple Kanban Board!
## Introduction
Simple Kanban Board is created to perform basic features of Kanban Board such as:
1. Creating a new task
2. Moving tasks to different states (todo, in progress, completed)
3. Deleting tasks
4. Registering a new user (Signup)
5. Authenticating as a user (Login)
6. Logging out while saving the session credentials

The Kanban Board is personlalized meaning that people can create their own Kanban boards and no-one else can view those Kanban boards.

## Structure of app

The root directory consists of the following files:

- `test.py`  - some unittests based on the covered topics.
- `requirements.txt` - the required packages for the project.
- `run.py`  - gets the app to run.

The `app` folder contains the application files:

- `__init__.py` - the configuration and initializes the app.
- `api.py` - routes for the navigation in the frontend pages.
- `models.py`  - connecting the database and the app.
- `templates/` is a folder which contains HTML templates.

There are also `css` and `scss` files containting the styling for the frontend pages made from HTML. 


## Intstalation
Follow the instractions bellow to run the app on your local machine:

1. Create virtual env
```bash
$ python3 -m venv .venv  
```
2. Activate the Virtual Environment
```bash
$ source .venv/bin/activate       # for Linux & macOS
$ env\Scripts\activate            # for Windows
```
3. Install all the requirements
```bash
$ pip3 install -r requirements.txt
```
4. Locate the root directory and run flask to start the webapp
```bash
$ cd kanban
$ export FLASK_APP=run.py
$ flask run
```

### Unit tests
#### Run unit tests
To run tests, while being in project's directory, run the following command:
```bash
$ python -m unittest discover test
```
        
        
### References used to make this webapp
- [Website Responsivness](https://www.w3schools.com/css/css_rwd_viewport.asp)
- [Making HTML Tables](https://www.w3schools.com/html/html_tables.asp)
- [Sortable elements](https://jqueryui.com/sortable/)
- [Emoji Reference](https://www.w3schools.com/charsets/ref_emoji.asp)
- [Creating a Todo List App With Flask and Flask-SQLAlchemy](https://www.youtube.com/watch?v=4kD-GRF5VPs)
- [Flask-login](https://flask-login.readthedocs.io/en/latest/)
- [Sessions in Flask](https://docs.sqlalchemy.org/en/14/orm/session_basics.html)
- [Structure of Flask Application](https://flask.palletsprojects.com/en/0.12.x/patterns/packages/)
        
        

