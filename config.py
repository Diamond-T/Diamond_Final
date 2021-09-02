import os



basedir = os.path.abspath(os.path.dirname(__file__))
class Config():
    FLASK_APP = 'run'
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = 'Diamonds key 1234'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')