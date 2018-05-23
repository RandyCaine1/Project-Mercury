from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired


class SignUpForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class StockForm(FlaskForm):
    stock = StringField('Symbol', validators=[InputRequired()])

class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
class SettingsForm(FlaskForm):
    investor_type = StringField('Investing Style: Growth or Value', validators=[InputRequired()])
    
class ContactForm(FlaskForm):
    subject = StringField('Subject', validators=[InputRequired()])
    message = StringField('Message', validators=[InputRequired()])
    
class BugForm(FlaskForm):
    subject = StringField('Subject', validators=[InputRequired()])
    message = StringField('Message', validators=[InputRequired()])
    