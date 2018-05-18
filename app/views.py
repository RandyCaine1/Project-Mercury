"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User
from app.models import *


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    #Initialization
    form = LoginForm()
    if request.method == "POST":
      
        if form.validate_on_submit():
            
            username = form.username.data
            password = form.password.data
            
            user = User.query.filter_by(username=username,password=password).first()
            if user is None:
                flash("Sorry, there is no such user.","warning")
            else:
                login_user(user)
                
                return redirect(url_for("dashboard")) 
    return render_template("login.html", form=form)
    
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("home"))
    

@app.route('/dashboard/portfolio')
@login_required
def dashboard():
    flash("Welcome back", "success")
    return render_template('dashboard/portfolio.html')
    
    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
