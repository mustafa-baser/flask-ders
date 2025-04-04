from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate(db=db)
login = LoginManager()
csrf = CSRFProtect()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    csrf.init_app(app)
