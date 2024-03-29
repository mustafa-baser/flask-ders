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
    return """
    
    <html>
    <head>
    <title>Günün Menüsü</title>
    </head>
    <body>
    <table border="1">
    <tr><th>Kahvaltı</th><th>Öğle Yemeği</th><th>Akşam Yemeği</th>
    <tr>
        <td>
            <ul>
                <li> Peynir
                <li> Zeytin
                <li> Yumurta
                <li> Çay
            </ul>
        </td>
        
        <td>
            <ul>
                <li> Çorba
                <li> Kuru fasulye
                <li> Pilav
                <li> Turşu
            </ul>
        </td>

        <td>
            <ul>
                <li> Salata
                <li> Makarna
                <li> Kadayıf
            </ul>
        </td>

    </tr>
    
    </table>
    </body>
    </html>
    
    
    
    
    """




app.run(debug=True)
