from flask import Blueprint

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.forms import LoginForm, RegisterForm
from app.models import db, User
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


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate(): 
        user = User(
            username=form.username.data,
            email=form.email.data,
            name=form.name.data,
            lastname=form.lastname.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Kayıtlanma tamamlandı", 'success')
        return redirect(url_for('auth.login'))
            
    return render_template('register.html', form=form)
