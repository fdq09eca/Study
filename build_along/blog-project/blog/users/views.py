from blog.users.pic_handler import add_profile_pic
import secrets
import os
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from blog import db
from blog.models import User, Post
from blog.users.forms import Reg_form, Login_form, Update_User_form
users = Blueprint('users',__name__)

#register
@users.route('/reg', methods=['post','get'])
def register():
    form = Reg_form()
    if form.validate_on_submit():
        new_user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Regisration success')
        return redirect(url_for(request.args.get('next','users.login')))
    return render_template('reg.html',form=form)
#login_view
@users.route('/login', methods=['post','get'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Login success')
            return redirect(url_for(request.args.get('next','core.index')))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)

#login_out
@login_required
@users.route(('/logout'))
def logout():
    logout_user()
    flash('Logout success')
    return redirect(url_for('core.index'))


@login_required
@users.route('/acc', methods=['GET', 'POST'])
def acc():
    form = Update_User_form()
    if form.validate_on_submit():
        if form.picture.data:
            # picture_file = save_picture(form.picture.data)
            picture_file = add_profile_pic(form.picture.data, form.username.data)
            current_user.profile_image = picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Account updated', 'success')
        return redirect(url_for('users.acc'))
    elif request.method == 'GET': #must be cap
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename='profile_img/'+current_user.profile_image)
    return render_template('acc.html', profile_image=profile_image, check=current_user.profile_image, form = form)

@login_required
@users.route('/<int:user_id>')
def user_posts(user_id):
    user = User.query.get_or_404(user_id)
    posts_by_users = Post.query.filter_by(author=user).order_by(Post.date.desc())
    # return render_template('user_page.html', posts_by_users=posts_by_users)
    return render_template('user_page.html', user=user, posts_by_users=posts_by_users)
