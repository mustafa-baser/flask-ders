from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
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

class PostForm(FlaskForm):
    body = TextAreaField("İleti", validators=[validators.InputRequired(message="Bu alan boş bırakılamaz")], render_kw={"rows": 5})
    submit = SubmitField("Gönder")

class CommentForm(FlaskForm):
    body = TextAreaField("Yorum", validators=[validators.InputRequired(message="Bu alan boş bırakılamaz")], render_kw={"rows": 5})
    submit = SubmitField("Gönder")

class ProfileForm(FlaskForm):
    avatar = FileField('Resim', validators=[FileAllowed(['jpeg', 'gif', 'jpg', 'png'], 'Sadece resim!')])
    name = StringField("Adı")
    lastname = StringField("Soyadı")
    about = StringField("Hakkında")
    birthdate = DateField("Doğum Tarihi", validators=[validators.InputRequired(message="Bu alan boş bırakılamaz")])
    submit = SubmitField("Kaydet")

class AvatarForm(FlaskForm):
    avatar = FileField('Resim', validators=[FileRequired(), FileAllowed(['jpeg', 'gif', 'jpg', 'png'], 'Sadece resim!')])
    submit = SubmitField('Yükle')


