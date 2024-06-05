from flask import Blueprint, render_template, request, redirect, url_for
from microblog.models import db, Post
from microblog.forms import PostForm

from flask_login import current_user

post_bp = Blueprint('post', __name__)


@post_bp.route('/new', methods=['GET', 'POST'])
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
def response(id):
    form = PostForm()

    post_obj = Post.query.get(id)
    msg = '{} tarafından yazılmış {} tarihli iletiye cevap'.format(post_obj.author.username, post_obj.date)

    if request.method == 'POST':
        post_obj = Post()
        post_obj.body = form.post.data
        current_user.posts.add(post_obj)
        db.session.commit()
        return redirect(url_for('index.index'))

    return render_template('post/post_form.html', form=form, msg=msg)
