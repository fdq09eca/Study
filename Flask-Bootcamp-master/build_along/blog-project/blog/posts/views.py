from flask import render_template, url_for, request, redirect, Blueprint, flash
from flask_login import current_user, login_required
from blog import db
from blog.models import Post
from blog.posts.forms import Post_form

posts = Blueprint('posts', __name__)

#create posts
@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = Post_form()
    if form.validate_on_submit():
        post = Post(title = form.title.data, text = form.text.data, user_id= current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post created', 'ok')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

#view posts
@posts.route('/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog_post.html', post = post)
# update posts
@posts.route('/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = Post_form()
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        db.session.commit()
        flash('Post updated', 'ok')
        return redirect(url_for('posts.view_post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
    return render_template('create_post.html', form=form)
#del posts
@posts.route('/<int:post_id>/del', methods = ['GET', 'POST'])
@login_required
def del_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'ng')
    return redirect(url_for('core.index'))
