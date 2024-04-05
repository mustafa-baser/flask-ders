from flask import Flask

from microblog.routes.index import index_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(index_bp, url_prefix='')

    return app
