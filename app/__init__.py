import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Initialize the app objects 
app = Flask(__name__) # create instance of the Flask class 
# Setup the directpry for the kanban.py
proj_dir = os.path.dirname(os.path.abspath(__file__))
# Setup database in the same directory as kanban.py file
db_path = "sqlite:///{}".format(os.path.join(proj_dir, "kanbandb.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = db_path
app.secret_key = "super secret"
signin = LoginManager()
signin.init_app(app)
signin.login_view = 'signin'
# Create database connection object
db = SQLAlchemy(app)



