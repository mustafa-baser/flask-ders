import os
import base64
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import current_user, login_user, logout_user, login_required

from microblog.models import db, User
from microblog.forms import LoginForm, RegistrationForm, ProfileForm


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(form.password.data):
                user.last_login = datetime.utcnow()
                db.session.commit()
                login_user(user)
                if not os.path.exists(user.upload_dir):
                    os.mkdir(user.upload_dir)

                flash("{} başarılı bir giriş yaptın".format(form.username.data))
                next_page = request.args.get('next') or url_for('index.index')
                return redirect(next_page)
            else:
                flash("Kullanıcı adı ya da parola hatalı")
        else:
            flash("Aşağaıda belirtilen alanlar eksik")

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("Zaten kayıtlısın")
        return redirect(url_for('index.index'))
    
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Kayıtlanma başarılı. Şimdi giril yapabilirsiniz.")
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@auth_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    form = ProfileForm()

    if request.method == 'POST':
        current_user.about_me = form.about_me.data
        current_user.email_public = form.email_public.data
        if form.avatar.data:
            avatar = form.avatar.data.stream.read()
            current_user.avatar = base64.encodebytes(avatar).decode()
        db.session.commit()
        flash("Profiliniz kaydedildi")

    else:
        form.about_me.data = current_user.about_me
        form.email_public.data = current_user.email_public
    
    return render_template('auth/profile_edit.html', form=form)


@auth_bp.route('/profile/show/<username>')
@login_required
def profile_show(username):
    puser = User.query.filter_by(username=username).first()
    if not puser:
        flash("Böyle bir kullanıcı mevcut değil")
        return redirect(url_for('index.index'))

    return render_template('auth/profile_show.html', puser=puser)
