from flask import Blueprint
from microblog.models import User

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    u = User.query.first()
    return "Merhaba {} - {} : {}".format(u.username, u.email, u.posts.first().body)

