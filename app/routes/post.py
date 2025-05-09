from datetime import datetime

from flask import Blueprint
from markupsafe import Markup

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from app.forms import PostForm, CommentForm
from app.models import db, Post, Comment
post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route('/posts')
@login_required
def posts():
    posts = current_user.posts.order_by(Post.timestamp.desc()).all()
    
    return render_template('post.html', posts=posts)

@post_bp.route('/posts/new-post', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if request.method == 'POST':
        if form.validate():
            post_obj = Post()
            post_obj.title = form.title.data
            post_obj.body = form.body.data
            current_user.posts.add(post_obj)
            db.session.commit()
            return redirect(url_for('post.posts'))
        else:
            flash("Gerekli alanları doldurmalısınız", 'danger')
    return render_template('post-form.html', form=form)



@post_bp.route('/posts/<int:pid>/new-comment', methods=['GET','POST'])
@login_required
def new_comment(pid):
    form = CommentForm()
    post_obj = Post.query.get(pid)

    if not post_obj:
        flash("Yorum yazılacak ileti bulunamadı", 'danger')
        return redirect(url_for('index.index'))

    if request.method == 'POST':
        if form.validate():
            comment_obj = Comment()
            comment_obj.body = form.body.data
            comment_obj.user_id = current_user.id
            post_obj.comments.add(comment_obj)
            db.session.commit()
            return redirect(url_for('index.index'))
        else:
            flash("Gerekli alanları doldurmalısınız", 'danger')

    title = Markup(f"<b>{post_obj.title}</b> başlıklı ileti için yorum")
    return render_template('post-form.html', form=form, title=title)
