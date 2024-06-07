from flask import Blueprint, render_template, request, redirect, url_for
from microblog.models import db, Post, PostComment
from microblog.forms import PostForm

from flask_login import current_user, login_required

post_bp = Blueprint('post', __name__)


@post_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()

    if request.method == 'POST':
        post_obj = Post()
        post_obj.body = form.post.data
        current_user.posts.add(post_obj)
        db.session.commit()
        return redirect(url_for('index.index'))

    return render_template('post/post_form.html', form=form)



@post_bp.route('/response/<int:id>', methods=['GET', 'POST'])
@login_required
def response(id):
    form = PostForm()

    post_obj = Post.query.get(id)

    if request.method == 'POST':
        comment_obj = PostComment()
        comment_obj.body = form.post.data
        comment_obj.user_id = current_user.id
        post_obj.comments.add(comment_obj)
        db.session.commit()
        return redirect(url_for('index.index'))

    return render_template('post/post_form.html', form=form, post=post_obj)
