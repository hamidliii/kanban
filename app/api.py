from app import db, app
from flask import render_template, redirect, request, g, session, flash
from flask_login import current_user, login_user, login_required
from .models import User, Task
from app import signin

# Setting the first page as sign in page
@app.route("/", methods=["GET", "POST"])

def initial_page():
    """
        This method redirects the users to the signin page.
    """
    return redirect("signin")

# Loading user object by user id from session
@signin.user_loader

def user_load(id):
    """
        This method loads the users by usage of user_loader.
    """

    return User.query.get(int(id))

# Route for registering new users 
@app.route('/signup', methods=['GET','POST'])

def signup():
    '''
        This method verifies the set conditions for password and registers users.
    '''
    if request.method == 'POST':
        # Verify that password length conditions are met or show an error message
        if len(request.form['password']) < 10:
            error = 'The password must be at least 10 characters long! Please enter new password.'
            return render_template('signup.html', error=error)
        # Verify that password and re-entery passwords are same or show an error message
        if request.form['password'] != request.form['re-enter']:
            error = 'Passwords do not match! Please enter again.'
            return render_template('signup.html', error=error)

        # Add new user username and password to db
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        # Redirect to signin page
        return redirect("/signin")

    elif request.method == 'GET':
        return render_template('signup.html')

# Route for signing in new users 
@app.route('/signin', methods=['GET', 'POST'])

def signin():
    ''' 
        This method verifies the credentials given by user and signs them in.
    '''
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        # Verify validity of credentials if not verified, show an error message 
        if user is None:
            error = 'Wrong credentials! Please, enter right credentials..'
            return render_template('signin.html', error=error)

        # Once a user has authenticated, log them in
        login_user(user)
        # Redirect to main page
        return redirect("/main")

    elif request.method == 'GET':
        return render_template('signin.html')

# Route for loging out of the session
@app.route('/logout', methods=['GET', 'POST'])

def logout():
    '''
        This method logs a user out of the current session and redirects to sign in page.
    '''
    session.pop('logged_in', None)
    # Redirect to signin page
    return redirect('signin')

# Route for main page (index.html)
@app.route('/main', methods=["GET", "POST"])
# Verifies that the user is authenticated/logged in
@login_required

def index():
    '''
        This method:
        1. Verifies uniquness of the task;
        2. Add the task to the Kanban Board & save in database;
        3. Filters the tasks by their status.
    '''

    # Variable initiation 
    g.user = current_user
    tasks = None
    error = None
    if request.form:
        try:
            # Verifies that given task is unqiue 
            if request.form.get("title") in [task.title for task in Task.query.all()]:
                error = "This task already exists."
            # If unique, add to the task to the database and the board
            else:
                new_id = len(Task.query.all()) + 1
                task = Task(id = new_id, title=request.form.get("title"), status=request.form.get("status"), user_id = g.user.id)
                tasks = Task.query.all()

                # Add new task to the session 
                db.session.add(task)
                # Commit the transaction to add new task permanently to the db 
                db.session.commit()
        # If an an error occurs, display it
        except Exception as e:
            print("Failed to add task")
            print(e)
            db.session.rollback()

    # Filter the tasks based on their status 
    tasks = Task.query.filter_by(user_id=g.user.id).all()
    todo = Task.query.filter_by(status='todo',user_id=g.user.id).all()
    progress = Task.query.filter_by(status='progress',user_id=g.user.id).all()
    completed = Task.query.filter_by(status='done',user_id=g.user.id).all()
    
    return render_template("index.html", error=error, tasks=tasks, todo=todo, progress=progress, completed=completed, myuser=current_user)

# Route for updating the tasks 
@app.route("/update", methods=["POST"])

def update():
    '''
        This method updates the task status by moving it to selected status section. 
    '''
    try:
        # Verify that the task can be updated 
        newstatus = request.form.get("newstatus")
        name = request.form.get("name")
        task = Task.query.filter_by(title=name).first()
        task.status = newstatus
        # Commit the transaction to update the status of task 
        db.session.commit()
    except Exception as e:
        # Display an error if the status can't be updated 
        print("Couldn't update task status")
        print(e)
        db.session.rollback()
    return redirect("/main")

# Route for deleting the tasks 
@app.route("/delete", methods=["POST"])

def delete():
    '''
        This method deletes the tasks. 
    '''
    title = request.form.get("title")
    task = Task.query.filter_by(title=title).first()
    # Mark the task for deletion to move the task to Session.deleted
    db.session.delete(task)
    # Commit the transaction to permanently delete the task 
    db.session.commit()
    return redirect("/main")
