from datetime import datetime
from flask_login import UserMixin
from flask import current_app

from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    profile = db.relationship('Profile', backref='user', lazy='dynamic')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        if self.id:
            db.session.commit()

    def __repr__(self):
        return f'<user {self.username} - {self.email}>'

    @property
    def avatar(self):
        result = self.profile.with_entities(Profile.avatar).first()
        if result and result[0]:
            return result[0]

        return current_app.config['DEFAULT_AVATAR']

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_me = db.Column(db.Text)
    avatar = db.Column(db.Text)
    birthdate = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
