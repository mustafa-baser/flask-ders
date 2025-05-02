from datetime import datetime

from flask import Blueprint

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from app.forms import PostForm
from app.models import db, Post
post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route('/posts')
@login_required
def posts():
    posts = current_user.posts.order_by(Post.timestamp.desc()).all()
    
    return render_template('post.html', posts=posts)

@post_bp.route('/new-post', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        post_obj = Post()
        post_obj.title = form.title.data
        post_obj.body = form.body.data
        current_user.posts.add(post_obj)
        db.session.commit()
        return redirect(url_for('post.posts'))
    else:
        flash("Gerekli alanları doldurmalısınız", 'danger')
    return render_template('post-form.html', form=form)
