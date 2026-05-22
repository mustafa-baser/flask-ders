from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_security import roles_accepted
from microblog.models import db, Post, Comment, User
from microblog.forms import PostForm, CommentForm
from flask_login import current_user, login_required
from microblog.routes.auth import role_required

post_bp = Blueprint('post', __name__)

@post_bp.route('/create', methods=['get', 'post'])
@login_required
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        post = Post(body = form.body.data)
        current_user.posts.add(post)
        db.session.commit()
        flash("İletiniz kaydedildi.", 'success')
        return redirect(url_for('index.index'))
    
    return render_template('post/post_create.html', form=form)


@post_bp.route('/comment', methods=['get', 'post'])
@login_required
def comment():
    form = CommentForm()
    post_id = request.args.get('id', int)
    post = Post.query.get(post_id)
    if request.method == 'POST' and form.validate():
        comment = Comment(body = form.body.data)
        comment.user_id = current_user.id
        post.comments.add(comment)
        db.session.commit()
        flash("Yorumunuz kaydedildi.", 'success')
        return redirect(url_for('index.index'))
    
    return render_template('post/post_comment.html', title="Yorum", form=form, post=post)

@post_bp.route('/messagenumber', methods=['get', 'post'])
@login_required
@role_required('admin')
def messagenumber():
    users = User.query.all()
    if request.method == 'POST':
        for user in users:
            user.daily_message_number = request.form.get(f'ileti-sayisi-{user.id}', int)
            db.session.commit()
    
    return render_template('post/post_messagenumber.html', title="Günlik İleti Sayısı", users=users)


@post_bp.route('/changemessagenumber')
@login_required
@role_required('admin')
def change_message_number():
    user_id = request.args.get('userid', int)
    mnumber = request.args.get('mnumber', int)
    user = User.query.get(user_id)
    if user:
        user.daily_message_number = mnumber
        db.session.commit()
        return 'true'
    return 'false'
