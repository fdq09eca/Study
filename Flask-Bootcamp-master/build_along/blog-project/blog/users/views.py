
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from blog import db
from blog.models import User, Post
from blog.users.forms import Reg_form, Login_form, Update_User_form
from blog.users.pic_handler import add_profile_pic

users = Blueprint('users', __name__)
# login view
# logout view
@users.route('/logout')
def logout():
    logout_user()
    flash('Logout successful.', category='ok')
    return redirect(url_for('core.index'))
# reg view

@users.route('/reg', methods=['GET', 'POST'])
def register():
    form = Reg_form()
    if form.validate_on_submit():
        users = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(users)
        db.session.commit()
        flash(message='Regisration successful.', category='ok')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)
#
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash(message='Login successful.', category='ok')
            return redirect(url_for(request.args.get('next', 'core.index')))
        else:
            flash('Invalid email or password', category='ng')
    return render_template('login.html', form = form)


@login_required
@users.route('/acc', methods=['get','post'])
def acc():
    form = Update_User_form()
    if form.validate_on_submit():
        flash('sumbit button.','ok')
        current_user.email=form.email.data
        current_user.username=form.username.data
        if form.picture.data:
            flash('Picture detect.','ok')
            flash(print(form.picture.data),'ok')
            current_user.profile_img = add_profile_pic(form.picture.data, current_user.username)
            flash('Pic Updated.','ok')
        flash('Account Updated.','ok')
        db.session.commit()
        return redirect(url_for('users.acc'))
    elif request.method =='GET': # if there is no update sumbition #must be cap
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_img = url_for('static', filename='profile_pics/' + current_user.profile_img)
    return render_template('acc.html', form=form, profile_img=profile_img)
# users list of blog posts

@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page',1,type=int) #paginate
    user = User.query.filter_by(username=username).first_or_404()
    posts_by_user = Post.query.filter_by(author=user).order_by(Post.date.desc()).paginate(page = page, per_page=5)
    return render_template('user_blog_posts.html', posts_by_user=posts_by_user, user=user)
