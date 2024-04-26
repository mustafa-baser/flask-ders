from flask import Blueprint, render_template, request, redirect, flash, url_for

auth_bp = Blueprint('auth', __name__)

from microblog.forms import LoginForm

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.username.data == 'serap' and form.password.data == '1234':
            flash("Giriş Başarılı")
            return redirect(url_for('index.index'))
        else:
            flash("Kullanıcı adı yada parolası yanlış")
    return render_template('auth/login_form.html', form=form)
