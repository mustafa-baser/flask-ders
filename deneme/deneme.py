import time
import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

class KullaniciEkleForm(FlaskForm):
    username = StringField('Kullanıcı Adı')
    email =  StringField('E-Posta Adresi')
    submit = SubmitField('Gönder')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ksjkcndhdksnb'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///microblog.sqlite3"


db = SQLAlchemy()
db.init_app(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)



@app.route('/')
def index():
    kullanici = {'adi': 'Hüsna', 'soyadi': 'Cömert'}
    iletiler = [
        {
            'yazar': {'adi': 'Yağmur'},
            'ileti': 'Ah şu MacOS çalışsa, neler yapacağım'
        },
        {
            'yazar': {'adi': 'Hüsna'},
            'ileti': 'Ben yapıyorum, bilgisayar çalışmıyor'
        },
        {
            'yazar': {'adi': 'Mustafa Hoca'},
            'ileti': 'Hiç kimseye bişey anlatamıyorum'
        },
    ]

    return render_template(
            'index.html', 
            kullanici=kullanici,
            saat='16:07',
            baslik="Giriş Sayfası",
            iletiler=iletiler
            )

@app.route('/kullanicilar')
def kullanicilar():    
    users = Users.query.all()

    return render_template(
            'kullanicilar.html',
            baslik="Kullanıcılar",
            kullanicilar=users
            )


@app.route('/kullaniciekle', methods=["GET", "POST"])
def kullaniciekle():

    form = KullaniciEkleForm()

    if request.method == 'POST':
        user = Users()
        user.username = form.username.data
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()

        return redirect("/kullanicilar")

    return render_template(
            'kullaniciekle.html',
            baslik="Kullanıcı ekleme formu",
            form=form
            )

@app.route('/kullanicisil')
def kullanicisil():
    sil_id = request.args.get('id')
    user = Users.query.get(int(sil_id))
    db.session.delete(user)
    db.session.commit()

    return redirect("/kullanicilar")

if __name__ == '__main__':
    app.run(debug=True)
