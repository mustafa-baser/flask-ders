from flask import Blueprint, render_template
from microblog.models import Post, User
from flask_login import current_user
index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():

    if current_user.is_authenticated:
        user_last_post = current_user.posts.order_by(Post.date.desc()).first()
        posts = Post.query.order_by(Post.date.desc()).filter(Post.user_id != current_user.id).limit(3).all()
    else:
        user_last_post = None
        posts=[]

    return render_template('index.html', user_last_post=user_last_post, posts=posts)
