import time
import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

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
    con = sqlite3.connect("microblog.sqlite3")
    cur = con.cursor()
    cur.execute("select * from users;")
    users = cur.fetchall()

    con.close()

    return render_template(
            'kullanicilar.html',
            baslik="Kullanıcılar",
            kullanicilar=users
            )


@app.route('/kullaniciekle', methods=["GET", "POST"])
def kullaniciekle():

    if request.method == 'POST':
        con = sqlite3.connect("microblog.sqlite3")
        cur = con.cursor()
        username = request.form["username"]
        email = request.form["email"]
        cur.execute(f"insert into users ('username', 'email') values ('{username}', '{email}');")
        con.commit()
        con.close()
        return redirect("/kullanicilar")
    
    return render_template(
            'kullaniciekle.html',
            baslik="Kullanıcı ekleme formu",
            )

app.run(debug=True)
