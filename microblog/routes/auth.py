from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from microblog.models import User
from microblog.forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index.index'))

        else:
            return "Kullanıcı adı yada parolası yanlış"
        return "Giriş işlemi yapılacak"
    else:
        return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
