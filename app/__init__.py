from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db_path = "sqlite:///kanban.db"

app.config["SQLALCHEMY_DATABASE_URI"] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret"

signin = LoginManager()
signin.init_app(app)
signin.login_view = 'signin'

db = SQLAlchemy(app)

from app import api