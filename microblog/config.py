import os

class Config(object):
    APP_DIR = os.path.dirname(__file__)
    UPLOAD_DIR = os.path.join(APP_DIR, 'upload')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'microblog.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'uzunca-tahmin-edilemeyen-bir-anahtar'
