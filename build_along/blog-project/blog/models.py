from blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String, nullable = True, server_default = 'default_profile_img.png')
    email = db.Column(db.String, unique = True, index = True)
    username = db.Column(db.String, unique = True, index = True)
    password_hash = db.Column(db.String)
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'username: {self.username}\n email: {self.email}'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

class Post(db.Model):
    __tablename__ = 'posts'
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key =True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id
    def __repr__(self):
        return f'Post id: {self.id}, Title:{self.title}'
