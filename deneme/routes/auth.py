from flask import Blueprint, render_template, request, url_for, redirect

from models import db, Users
from forms import KullaniciEkleForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return "Auth Index"


@auth_bp.route('/register')
def register():
    return "Kayutlanma burda"


@auth_bp.route('/kullanicilar')
def kullanicilar():
    users = Users.query.all()

    return render_template(
            'auth/kullanicilar.html',
            baslik="Kullanıcılar",
            kullanicilar=users
            )


@auth_bp.route('/kullaniciekle', methods=["GET", "POST"])
def kullaniciekle():

    form = KullaniciEkleForm()

    if request.method == 'POST':
        user = Users()
        user.username = form.username.data
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.kullanicilar'))

    return render_template(
            'auth/kullaniciekle.html',
            baslik="Kullanıcı ekleme formu",
            form=form
            )

@auth_bp.route('/kullanicisil')
def kullanicisil():
    sil_id = request.args.get('id')
    user = Users.query.get(int(sil_id))
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('auth.kullanicilar'))
