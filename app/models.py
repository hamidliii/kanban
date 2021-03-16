from app import db
from flask_login import UserMixin

# Define models
# Create and initialize User and Task objects

class Task(db.Model):
    """
        This class:
        1. Initializes the task name and status;
        2. Connects the task to user id.
    """
    __tablename__ = "Task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  unique = True, nullable=False)
    status = db.Column(db.String(15), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    def __repr__(self):
        return "<Title: {}>".format(self.title)

class User(UserMixin, db.Model):
    '''
        This class initializes user name, password and related tasks.
    '''
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50))
    task_id = db.relationship('Task', backref='user', lazy='dynamic')
    def __repr__(self):
        return "<Username: {}>".format(self.username)


# Create database for users & tasks
db.create_all()
# Create entries for each table in the database
db.session.commit()
