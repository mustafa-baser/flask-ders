# Veritabanı modellerini burada tanımlayın
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_security import RoleMixin

from microblog.extensions import db, login


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    daily_message_number = db.Column(db.Integer, default=5)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    profile = db.relationship('Profile', backref='user', uselist=False)
    roles = db.relationship('RolesUsers', backref='author', lazy='dynamic')

    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def has_role(self, role_required):
        for role in self.roles:
            if role.roleobj.name == role_required:
                return True
        return False

    def __repr__(self):
        return f"< {self.username} - {self.email} >"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='post', lazy='dynamic')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String)
    avatar = db.Column(db.String)
    birthdate = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)  

    role = db.relationship('RolesUsers', backref='roleobj', lazy='dynamic')

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

