from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "aDAFNSJgjndjfbknkjcbkBFBBIBIdrsfgdfznmdVBVIVBNVDKJVBDF"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mercury:group15@localhost/mercury"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views