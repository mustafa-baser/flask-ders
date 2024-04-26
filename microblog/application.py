from flask import Flask
from microblog.config import Config
from microblog.routes.index import index_bp
from microblog.routes.auth import auth_bp
from microblog.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # eklentiler
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(index_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='/auth')



    return app
