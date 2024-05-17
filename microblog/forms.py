from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from microblog.models import User

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    submit = SubmitField("Gir")

class RegisterForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[DataRequired()])
    password = PasswordField("Parola", validators=[DataRequired()])
    password1 = PasswordField("Tekrar Parola", validators=[DataRequired()])
    email = StringField("E-posta", validators=[DataRequired()])
    submit = SubmitField("Üye Ol")
    
    def validate_username(self, field):
        if len(field.data) < 5:
            raise ValidationError('Kullanıcı adı en az 5 karakter olmalı')

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Bu kullanıcı adı ile kayıtlanmaya izin verilmiyor')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Bu e-posta adresi ile kayıtlanmaya izin verilmiyor')
    
    def validate_password(self, field):
        if len(field.data) < 3:
            raise ValidationError('Parola en az 3 karakter olmalı')
            
    def validate_password1(self, field):
        if self.password.data != field.data:
            raise ValidationError('Parolalar uyuşmuyor')
            

class ProfileForm(FlaskForm):
    name = StringField("Adı")
    lastname = StringField("Soyadı")
    about = TextAreaField("Hakkımda")
    submit = SubmitField("Güncelle")
