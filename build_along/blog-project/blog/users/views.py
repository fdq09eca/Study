from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from blog import db
from blog.models import User
from blog.users.forms import Reg_form, Login_form
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
