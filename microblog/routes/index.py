from flask import Blueprint, render_template
from microblog.models import User

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    user = User.query.first()
    posts = user.posts.all()

    return render_template('index/index.html', user=user, posts=posts)

