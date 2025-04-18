from flask import Blueprint

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.forms import LoginForm
from app.models import User
from app.extensions import login


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Giriş başarılı", 'success')
            return redirect(url_for('index.index'))
        else:
            flash("Kullanıcı adı veya parolası yanlış", 'danger')

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("Çıkış başarılı", 'success')
    return redirect(url_for('index.index'))
