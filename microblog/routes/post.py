from flask import Blueprint, render_template, request, flash, redirect, url_for
from microblog.models import db, Post
from microblog.forms import PostForm
from flask_login import current_user

post_bp = Blueprint('post', __name__)


@post_bp.route('/create', methods=['get', 'post'])
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        post = Post(body = form.body.data)
        current_user.posts.add(post)
        db.session.commit()
        flash("İletiniz kaydedildi.", 'success')
        return redirect(url_for('index.index'))
    
    return render_template('post/post_create.html', form=form)

