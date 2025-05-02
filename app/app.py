from flask import Flask, render_template, request

from app.config import Config

from app.routes.index import index_bp
from app.routes.auth import auth_bp
from app.routes.post import post_bp


from app.extensions import init_extensions 

def create_app():

    app = Flask(__name__)
    
    # yapılandırma nesnesi
    app.config.from_object(Config)
    
    # bluebrintler
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)


    # uzantıları başlat
    init_extensions(app)
    
    return app

