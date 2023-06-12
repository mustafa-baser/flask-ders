from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField,\
    TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


from microblog.models import db, User

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(message="Bu alan gerekli")])
    password = PasswordField('Parola', validators=[DataRequired(message="Bu alan gerekli")])
    remember_me = BooleanField('Beni hatırla')
    submit = SubmitField('Giriş')


class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(message="Bu alan gerekli")])
    email = StringField('E-Posta', validators=[DataRequired(message="Bu alan gerekli"), Email(message="Geçerli bir e-posta adresi girin")])
    password = PasswordField('Parola', validators=[DataRequired(message="Bu alan gerekli")])
    password2 = PasswordField('Parola Tekrar', validators=[DataRequired(message="Bu alan gerekli"), EqualTo('password', message="Parola ile aynı olmalı")])
    submit = SubmitField('Kayıtlan')


    def validate_username(self, username):
        if len(username.data.strip()) < 3:
            raise ValidationError("Kullanıcı adı en az üç karakter olmalı")

        user = User.query.filter_by(username=username.data).first()
        if user or '@' in username.data.strip():
            raise ValidationError("Geçersiz kullanıcı adı")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Bu e-posta adresi kayıtlı")

class ProfileForm(FlaskForm):
    avatar = FileField("Avatar")
    about_me = TextAreaField('Hakkımda')
    email_public = BooleanField('E-posta adresim görünsün')
    submit = SubmitField('Kaydet')

class MessageForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired(message="Bu alan gerekli")])
    body = TextAreaField('İleti')
    submit = SubmitField('Kaydet')

class MessageCommentForm(FlaskForm):
    body = TextAreaField('İleti')
    submit = SubmitField('Kaydet')


class MailForm(FlaskForm):
    receiver = SelectField('Alıcı', choices=[])
    title = StringField('Başlık', validators=[DataRequired(message="Bu alan gerekli")])
    body = TextAreaField('İleti', render_kw = {'rows': '10'})
    submit = SubmitField('Gönder')

    def __init__(self):
        super(MailForm, self).__init__()
        userlist = User.query.filter(User.id != current_user.id).order_by(User.username.asc()).all()
        self.receiver.choices = [(str(user.id), user.username) for user in userlist]

class FileUploadForm(FlaskForm):
    file_upload = FileField("Dosya")
    submit = SubmitField('Yükle')

