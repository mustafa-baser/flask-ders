from flask import Blueprint, render_template
from microblog.models import User, Post
from flask_login import current_user

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).limit(5).all()
    return render_template('index/index.html', posts=posts)

