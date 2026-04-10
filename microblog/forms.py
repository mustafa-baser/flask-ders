from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, validators
from microblog.models import User
# formları burada oluşturun

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[validators.InputRequired(message="Bu alan boş bırakılamaz")])
    password = PasswordField("Parola", validators=[validators.InputRequired(message="Bu alan boş bırakılamaz")])
    submit = SubmitField("Giriş")


class RegisterForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=4, max=25)])
    password = PasswordField("Parola", validators=[validators.Length(min=6)])
    password2 = PasswordField("Parola Tekrar", validators=[validators.EqualTo('password', message="Parola uyuşmuyor")])
    name = StringField("Adı")
    lastname = StringField("Soyadı")
    email = StringField("E-posta", validators=[validators.Email(message="Lütfen geçerli bir e-posta adresi girin.")])
    submit = SubmitField("Kayıt Ol")


    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise validators.ValidationError("Bu kullanıcı adı mevcut")

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise validators.ValidationError("Bu e-posta adresi ile başka bir kullanıcı kayıtlı.")
