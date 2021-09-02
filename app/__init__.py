from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import Config 
from flask_login import LoginManager
#setting up database
app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models 



