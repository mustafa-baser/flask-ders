from flask import Blueprint
from functools import wraps

from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_login import current_user, login_required

from app.models import db, Post
index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/')
@index_bp.route('/<int:current_page>')
def index(current_page=1):

    title = 'BÖTE Ders Bloğu'
    page = db.paginate(db.select(Post).order_by(Post.timestamp.desc()), per_page=10, page=current_page)
    
    return render_template('index.html', title=title, page=page, current_page=current_page)
    

@index_bp.route('/test')
def test():
    return "TEST ROUTE"

@index_bp.route('/nedir')
def nedir():
    return "Nedir Bu?"



def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.has_role(role):
                return f(*args, **kwargs)
            abort(401, "Buraya erişiminiz yok")
            
        return decorated_function
    return decorator


@index_bp.route('/admin-pages')
@login_required
@role_required('admin')
def admin_pages():
    if current_user.username != 'melike':
        flash("Erişim engeli", 'danger')
        return redirect(url_for('index.index'))

    return render_template('admin.html')
