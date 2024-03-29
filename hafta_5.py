from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Geçmiş olsun Çağla"

@app.route('/saat')
def saat():
    return f"<b>Bugünkü tarih: </b> {time.ctime()}"

@app.route('/yemek-menusu')
def yemek_menusu():
    html_metin = open('yemek_menusu.html').read()
    return html_metin
    


app.run(debug=True)
