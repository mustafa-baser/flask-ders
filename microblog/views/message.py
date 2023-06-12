from flask import Blueprint, render_template, request, flash,\
    redirect, url_for
from flask_login import login_required, current_user

from microblog.models import db, Post, PostComment
from microblog.forms import MessageForm, MessageCommentForm

message_bp = Blueprint('message', __name__)


@message_bp.route('/')
@login_required
def index():

    title = "İletiler"

    #posts = Post.query.order_by(Post.timestamp.desc()).limit(5)

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=10, error_out=False)

    return render_template('message/index.html', title=title, posts=posts)


@message_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():

    title = "Yeni İleti"
    form = MessageForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_post = Post(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash("İletiniz kaydedildi")
        next_page = request.args.get('next') or url_for('message.index')
        return redirect(next_page)

    return render_template('message/new.html', title=title, form=form)

@message_bp.route('/comment/<int:pid>', methods=['GET', 'POST'])
@login_required
def comment(pid):

    title = "İletiye Yorum"
    form = MessageCommentForm()
    post = Post.query.get(pid)

    if request.method == 'POST':
        new_comment = PostComment(body=form.body.data, user_id=current_user.id, post_id=pid)
        db.session.add(new_comment)
        db.session.commit()
        flash("Yorumunuz eklendi")
        next_page = request.args.get('next') or url_for('message.index')
        return redirect(next_page)

    return render_template('message/comment.html', title=title, form=form, post=post)
