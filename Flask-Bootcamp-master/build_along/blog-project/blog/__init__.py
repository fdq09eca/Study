import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from blog.core.views import core
from blog.error_pages.handlers import error_pages
app = Flask(__name__)
app.register_blueprint(core)
app.register_blueprint(error_pages)

# Database setup
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
Migrate(app, db)

#Login config setup

login_manager = LoginManager()
login_manager.login_view = 'users.login' #gonna connect with the Blueprint file users which has a view function names login
login_manager.init_app(app)
