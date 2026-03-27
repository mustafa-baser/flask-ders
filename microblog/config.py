import os

class Config:
    BASEDIR = os.path.dirname(__file__)
    SECRET_KEY = 'bu-gizli-anahtari-degistirin'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'microblog.sqlite3')
