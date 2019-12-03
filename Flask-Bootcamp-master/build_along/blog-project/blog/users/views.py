
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


# account view(Update_User_form)
# users list of blog posts
