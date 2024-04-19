from flask import Blueprint, render_template, request, redirect

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    error = ''
    if request.args:
        if request.args['username'] == 'serap' and request.args['password'] == '1234':
            return redirect('/')
        else:
            error = "Kullanıcı adı yada parolası yanlış"
    return render_template('auth/login_form.html', error=error)
