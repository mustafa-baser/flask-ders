from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")
    submit = SubmitField("Giriş")
