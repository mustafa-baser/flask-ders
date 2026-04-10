from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from microblog.models import db, User
from microblog.forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first() or User.query.filter_by(email=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Giriş başarılı")
            return redirect(url_for('index.index'))

        flash("Kullanıcı adı yada parolası yanlış")

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
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

        flash("Kullanıcı kayıtlanması tamam. Giriş yapabilirsiniz.")
        return redirect(url_for('auth.login'))


    return render_template('auth/register.html', form=form)
