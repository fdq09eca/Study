from myproject import db, login_man
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_man.user_loader
def load_user(user_id):
    return db.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__  = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64), unique=True, index = True) # no two users with the same email.
    username = db.Column(db.String(64), unique=True, index = True) # no two users with the same name.
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
