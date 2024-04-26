import os

class Config:
    SECRET_KEY = 'uzunca-ve-kimse-tarafindan-tahmin-edilemeyecek-anahtar'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'microblog.sqlite3')
