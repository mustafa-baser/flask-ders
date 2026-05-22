import base64
from functools import wraps

from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import current_user, login_user, logout_user, login_required

from microblog.models import db, User, Profile
from microblog.extensions import login
from microblog.forms import LoginForm, RegisterForm, ProfileForm, AvatarForm

auth_bp = Blueprint('auth', __name__)


def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_role(role):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first() or User.query.filter_by(email=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            redirect_url = request.args.get('next') or url_for('index.index')
            flash("Giriş başarılı", 'success')
            return redirect(redirect_url)

        flash("Kullanıcı adı yada parolası yanlış", 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        user = User()
        user.username = username
        user.name = name
        user.lastname = lastname
        user.email = email
        db.session.add(user)
        db.session.commit()
        user.set_password(password)

        flash("Kullanıcı kayıtlanması tamam. Giriş yapabilirsiniz.", 'success')
        return redirect(url_for('auth.login'))


    return render_template('auth/register.html', form=form)

@auth_bp.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm()
    if not current_user.profile:
        current_user.profile = Profile()
        db.session.commit()

    if request.method == 'POST' and form.validate():
        if 'avatar' in request.files:
            avatar_file_obj = request.files.get('avatar')
            avatar_str = avatar_file_obj.read()
            if len(avatar_str) > 100:
                current_user.profile.avatar = base64.encodebytes(avatar_str).decode()
        current_user.name = form.name.data
        current_user.lastname = form.lastname.data
        current_user.profile.about = form.about.data
        current_user.profile.birthdate = form.birthdate.data
        db.session.commit()
        flash("Değişiklikler Kaydedildi.", 'success')
        return redirect(url_for('auth.profile'))
        
    else:
        form.name.data = current_user.name
        form.lastname.data = current_user.lastname
        form.about.data = current_user.profile.about
        form.birthdate.data = current_user.profile.birthdate
    
    return render_template('auth/profile.html', title="Profil", form=form)

@auth_bp.route('/profile/avatar/delete', methods=["GET"])
@login_required
def profile_avatar_delete():
    form = ProfileForm()
    current_user.profile.avatar = ''
    db.session.commit()
    flash("Avatar silindi.", 'success')
    return redirect(url_for('auth.profile'))
