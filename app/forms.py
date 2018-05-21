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
    stock = StringField('Stock', validators=[InputRequired()])
    

class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
class SettingsForm(FlaskForm):
    growth = BooleanField('Growth')
    value = BooleanField()
    daytrader = BooleanField()
    swingtrader = BooleanField()
    position = BooleanField()
    
    
    
    