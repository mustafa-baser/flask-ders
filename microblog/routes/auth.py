from flask import Blueprint, render_template, request, redirect, flash, url_for

auth_bp = Blueprint('auth', __name__)

from microblog.models import User
from microblog.forms import LoginForm

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_obj = User.query.filter_by(username=form.username.data).first()
        if user_obj and user_obj.check_password(form.password.data):
            flash("Giriş Başarılı")
            return redirect(url_for('index.index'))
        else:
            flash("Kullanıcı adı yada parolası yanlış")
    return render_template('auth/login_form.html', form=form)
