from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
migrate = Migrate(db=db)
login = LoginManager()
login.login_view = 'auth.login'

csrf = CSRFProtect()
bootstrap = Bootstrap5()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    csrf.init_app(app)
    bootstrap.init_app(app)
