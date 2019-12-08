from flask import render_template, request, Blueprint
from blog.models import Post
core = Blueprint('core', __name__)
@core.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
@core.route('/info')
def info():
    return render_template('info.html')