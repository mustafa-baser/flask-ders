from flask import Blueprint, render_template
from flask_login import login_required, current_user

from microblog.models import db, User, Post

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@login_required
def index():

    title = "Benim Süper Sayfam"

    posts = current_user.posts.order_by(Post.timestamp.desc()).limit(5)

    return render_template('index/index.html', title=title, posts=posts)

@index_bp.route('/deneme')
def deneme():
    return "İşte bir deneme"


@index_bp.app_template_filter()
def uppercase(text):
    return text[0]+'***'+text[-1]
