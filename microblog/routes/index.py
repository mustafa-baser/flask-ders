from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    user = {'username': 'cagla'}
    return render_template('index.html', user=user)
