from flask import Flask

from microblog.config import Config
from microblog.routes.index import index_bp
from microblog.routes.auth import auth_bp
from microblog.extensions import init_extensions


def create_app():
    app = Flask(__name__)

    # Uygulama yapılandırılıyor
    app.config.from_object(Config)

    init_extensions(app)

    # Blueprint'ler burada kayıtlanıyor
    app.register_blueprint(index_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
