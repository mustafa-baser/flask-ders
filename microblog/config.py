import os

class Config:
    SECRET_KEY = 'uzunca-ve-kimse-tarafindan-tahmin-edilemeyecek-anahtar'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'microblog.sqlite3')
    MAX_CONTENT_LENGTH = 1024 *1024 *1024
