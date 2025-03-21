import os

class Config:
    BASEDIR = os.path.dirname(__file__)
    SECRET_KEY = 'rastgele-uzunca-bir-string-aösjdhahasdjfhaöjsdfgaçmbfmsdfhyraçwkfjbömas'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'microblog.sqlite3')
