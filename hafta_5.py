from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Geçmiş olsun Çağla"

@app.route('/saat')
def saat():

    tarih = time.ctime()
    gun = 'Cuma'
        
    return render_template('tarih_saat.html', tarih=tarih, gun=gun)


@app.route('/yemek-menusu')
def yemek_menusu():
    data = {
        'tarih': time.ctime(),
        'kahvalti': ['Kaşar', 'Zeytin', 'Mıhlama', 'Çay', 'Bal', 'Tereyağ'],
        'ogle': ['Dürüm döner', 'Salata', 'Cacık', 'Puding'],
        'aksam': ['Salata', 'Makarna', 'Sütlaç'],
        }
        
    return render_template('yemek_menusu.html', data=data)


app.run(debug=True)
