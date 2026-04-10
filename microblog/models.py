# Veritabanı modellerini burada tanımlayın
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def __repr__(self):
        return f"< {self.username} - {self.email} >"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
