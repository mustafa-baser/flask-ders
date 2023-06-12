import os
import time
from flask import Flask

from microblog.errors import error_bp
from microblog.views.index import index_bp
from microblog.views.auth import auth_bp
from microblog.views.message import message_bp
from microblog.views.mail import mail_bp
from microblog.views.files import files_bp


from microblog.config import Config
from microblog.extensions import db, migrate, login, bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join(app.config['APP_DIR'], 'migrations'))
    login.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(error_bp, url_prefix='/errors')
    app.register_blueprint(index_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(message_bp, url_prefix='/message')
    app.register_blueprint(mail_bp, url_prefix='/mail')
    app.register_blueprint(files_bp, url_prefix='/files')

    
    @app.template_filter()
    def get_time(timestamp):
        return time.ctime(timestamp)

    return app
