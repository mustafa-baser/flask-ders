from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Geçmiş olsun Çağla"

@app.route('/saat')
def saat():

    data = {'tarih': time.ctime(), 'gun': 'Cuma'}
    template = "<b>Bugünkü tarih: </b> {tarih}, günlerden {gun}"
    
    return template.format(**data)


@app.route('/yemek-menusu')
def yemek_menusu():
    html_metin = open('yemek_menusu.html').read()
    data = {
        'tarih': time.ctime(),
        'kahvalti_1': 'Peynir',
        'kahvalti_2': 'Zeytin',
        'kahvalti_3': 'Mıhlama',
        'kahvalti_4': 'Çay',
        }
    return html_metin.format(**data)
    


app.run(debug=True)
