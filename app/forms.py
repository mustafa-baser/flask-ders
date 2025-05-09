from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms import DateField
 
from wtforms.validators import InputRequired, ValidationError, EqualTo, Email, Length

from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")
    submit = SubmitField("Giriş")


class RegisterForm(FlaskForm):
    username = StringField("Kullanıcı Adı*", validators=[InputRequired(), Length(min=4, message="Kullanıcı adı en az 3 karakter olmalı")])
    password = PasswordField("Parola*", 
            validators=[InputRequired(), 
                        Length(min=4, message="Parola en az 4 karakter olmalı"),
                        EqualTo('password2', message='Parolalar uyuşmuyor.')
                        ])
    password2 = PasswordField("Parola (tekrar)*", validators=[InputRequired()])
    name = StringField("Adınız")
    lastname = StringField("Soyadınız")
    email = StringField("E-posta", validators=[InputRequired(), Email(message="Lütfen geçerli bir e-posta adresi girin.")])
    submit = SubmitField("Kayıt Ol")


    def validate_username(self, field):
        user_exists = User.query.filter_by(username=field.data).first()
        if user_exists:
            raise ValidationError("Bu kullanıcı adı mevcut lütfen başka bir ad seçin.")

    
    def validate_email(self, field):
        email_exists = User.query.filter_by(email=field.data).first()
        if email_exists:
            raise ValidationError("Bu e-posta adresi ile daha önceden kayıtlanma yapılmış.")

class ProfilForm(FlaskForm):
    about_me = TextAreaField("Hakkımda")
    avatar = FileField("Avatar")
    birthdate = DateField("Doğum Tarihi")
    submit = SubmitField("Kaydet")

class PostForm(FlaskForm):
    title = StringField("Başlık")
    body = TextAreaField("İleti", validators=[InputRequired()])
    submit = SubmitField("Gönder")

class CommentForm(FlaskForm):
    body = TextAreaField("Yorum", validators=[InputRequired()])
    submit = SubmitField("Gönder")
