from flask import Blueprint, render_template
from microblog.models import User
from flask_login import current_user

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index/index.html')

