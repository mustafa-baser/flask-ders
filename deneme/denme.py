import time
from flask import Flask
from flask import render_template

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

app.run(debug=True)
