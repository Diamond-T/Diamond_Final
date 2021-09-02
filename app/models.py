from app import db
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


#creating the class for video games
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))