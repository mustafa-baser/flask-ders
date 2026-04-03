import os

class Config:
    BASEDIR = os.path.dirname(__file__)
    SECRET_KEY = '8a88e1ab-0166-458d-9ca6-e946224fc7f1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'microblog.sqlite3')
