import os
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
from microblog.extensions import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_login = db.Column(db.DateTime())

    #profil
    about_me = db.Column(db.String(250))
    email_public = db.Column(db.Boolean())
    avatar = db.Column(db.Text())

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('PostComment', backref='author', lazy='dynamic')
    received_messages = db.relationship('Message', backref='receiver', foreign_keys='Message.receiver_id', lazy='dynamic')
    sent_messages = db.relationship('Message', backref='sender', foreign_keys='Message.sender_id', lazy='dynamic')


    @property
    def upload_dir(self):
        return os.path.join(current_app.config['UPLOAD_DIR'], str(self.id))

    def unread_messages_count(self):
        return self.received_messages.filter_by(read=False).count()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('PostComment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class PostComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.body)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    read = db.Column(db.Boolean(), default=False)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '<Message {}>'.format(self.title)
