from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    user = {'username': 'cagla'}
    
    posts = [
        {'author': 'serap', 'body': "Kastamonu kanyonuna geldiniz mi?"},
        {'author': 'sumeyra', 'body': "Asıl Vezirköprü kanyonunu gödrünüz mü?"},
        {'author': 'gulsat', 'body': "Herkes acıktı hcoam gidelim"},
    ]
    
    return render_template('index.html', user=user, posts=posts)
