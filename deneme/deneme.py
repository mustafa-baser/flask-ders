import time
import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect

from config import Config
from extensions import init_extensions, db
from routes.auth import auth_bp


app = Flask(__name__)
app.config.from_object(Config)
init_extensions(app)

app.register_blueprint(auth_bp, url_prefix='/auth')



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



if __name__ == '__main__':
    app.run(debug=True)
