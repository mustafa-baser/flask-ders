from flask import Blueprint

from flask import Flask, render_template, request
from app.models import Post
index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/')
def index():

    title = 'BÖTE Ders Bloğu'
    posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()


    return render_template('index.html', title=title, posts=posts)
    

@index_bp.route('/test')
def test():
    return "TEST ROUTE"

@index_bp.route('/nedir')
def nedir():
    return "Nedir Bu?"
