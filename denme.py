from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    s="""
<html>
    <head>
        <title>Ana Sayfa - Microblog</title>
    </head>
    <body>
        <h1>Merhaba, {adi}!</h1>
        Şu an saat {saat}
    </body>
</html>
"""

    kullanici = {'adi': 'Hüsna', 'saat': '13:30'}
    return s.format(**kullanici)


app.run(debug=True)
