import base64

from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user

auth_bp = Blueprint('auth', __name__)

from microblog.models import User, Profile
from microblog.forms import LoginForm, RegisterForm, ProfileForm
from microblog.extensions import db, login

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_obj = User.query.filter_by(username=form.username.data).first()
        if user_obj and user_obj.check_password(form.password.data):
            flash("Giriş Başarılı", category='success')
            login_user(user_obj)
            return redirect(url_for('index.index'))
        else:
            flash("Kullanıcı adı yada parolası yanlış", category='danger')
    return render_template('auth/login_form.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("Başarılı bir şekilde çıkış yaptınız.", category='success')
    return redirect(url_for('index.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password1 = form.password1.data
            email = form.email.data
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            user.set_password(password)
            flash("Kayıtlanma başarılı", category='success')
            return redirect(url_for('index.index'))

    return render_template('auth/register_form.html', form=form)

@auth_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    form =  ProfileForm()
    if request.method == 'POST':
        if not current_user.profile:
            current_user.profile = Profile()

        current_user.profile.name = form.name.data
        current_user.profile.lastname = form.lastname.data
        current_user.profile.about = form.about.data
        
        if 'avatar' in request.files:
            avatar_bin = request.files['avatar'].stream.read()
            avatar_str = base64.encodebytes(avatar_bin).decode()
            current_user.profile.avatar = avatar_str
        
        db.session.commit()

    else:
        if current_user.profile:
            form.name.data = current_user.profile.name
            form.lastname.data = current_user.profile.lastname
            form.about.data = current_user.profile.about

    return render_template('auth/profile_form.html', form=form)


@auth_bp.route('/profile-delete')
def profile_delete():
    if current_user.profile:
        current_user.profile.avatar = None
        db.session.commit()
    return redirect(url_for('auth.profile'))
