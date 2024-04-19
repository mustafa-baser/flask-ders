from flask import Blueprint, render_template, request, redirect, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    if request.args:
        if request.args['username'] == 'serap' and request.args['password'] == '1234':
            flash("Giriş Başarılı")
            return redirect('/')
        else:
            flash("Kullanıcı adı yada parolası yanlış")
    return render_template('auth/login_form.html')
