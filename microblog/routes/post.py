from flask import Blueprint, render_template, request, flash, redirect, url_for
from microblog.models import db, Post, Comment
from microblog.forms import PostForm, CommentForm
from flask_login import current_user, login_required

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
