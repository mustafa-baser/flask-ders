from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth', __name__)

from microblog.models import User
from microblog.forms import LoginForm
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
            flash("Giriş Başarılı")
            login_user(user_obj)
            return redirect(url_for('index.index'))
        else:
            flash("Kullanıcı adı yada parolası yanlış")
    return render_template('auth/login_form.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("Başarılı bir şekilde çıkış yaptınız.")
    return redirect(url_for('index.index'))
