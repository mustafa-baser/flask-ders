# Eklentileri buarada başlatın
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
migrate = Migrate(db=db)
login = LoginManager()
bootstrap = Bootstrap5()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)
