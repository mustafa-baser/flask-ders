from flask import Flask

from sample.config import Config
from sample.routes.index import index_bp



def create_app():
    app = Flask(__name__)

    # Uygulama yapılandırılıyor
    app.config.from_object(Config)

    # Eklentileri burada etkinleştirin
    # Örnek: eklenti.init_app(app)


    # Blueprint'ler burada kayıtlanıyor
    app.register_blueprint(index_bp, url_prefix='')

    return app
