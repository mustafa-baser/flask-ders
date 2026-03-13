from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class KullaniciEkleForm(FlaskForm):
    username = StringField('Kullanıcı Adı')
    email =  StringField('E-Posta Adresi')
    submit = SubmitField('Gönder')

