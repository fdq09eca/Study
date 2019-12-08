from flask import Blueprint, url_for, render_template, request, flash, redirect, abort
from flask_login import login_required, current_user
from blog.models import Post
from blog.posts.forms import Create_form
from blog import db
posts = Blueprint('posts', __name__)

# create post
@posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = Create_form()
    if form.validate_on_submit():
        post=Post(title = form.title.data, text = form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post created.')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)
# update post
@login_required
@posts.route('/<int:post_id>/update', methods=['GET','POST'])
def update(post_id):
    form = Create_form()
    post = Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        if post.author!=current_user:
            abort(403)
        post.title = form.title.data
        post.text = form.content.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('posts.view_post', post_id=post.id))
    elif request.method =='GET':
        form.title.data = post.title
        form.content.data = post.text
    return render_template('create_post.html', form=form)

# view post
@posts.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

# delete post
@login_required
@posts.route('/<int:post_id>/del',methods=['POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('core.index'))
