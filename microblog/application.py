from flask import Flask
from microblog.config import Config
from microblog.routes.index import index_bp
from microblog.routes.auth import auth_bp
from microblog.routes.post import post_bp

from microblog.extensions import db, migrate, login, bootstrap


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # eklentiler
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    app.register_blueprint(index_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/post')



    return app
