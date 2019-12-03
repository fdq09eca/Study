from project import app, db, login_manager
from project.forms import Login_form, Reg_form, Del_form
from project.models import User
from flask import render_template, flash, session, redirect, url_for, request, abort
from flask_login import login_required, login_user, logout_user, current_user


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or user.check_password(form.password.data) is False:
            flash('Invalid password or email')
        elif user.check_password(form.password.data):
            login_user(user)
            flash('Login successful.')
            next = request.args.get('next')
            if next==None: #?
                return redirect(url_for('user_database'))
            else:
                return redirect(url_for('error404'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = Reg_form()
    if form.validate_on_submit():
        new_user = User(email = form.email.data,
                        username = form.username.data,
                        password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registerion success, you may login now.')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash('Logout successful.')
    return redirect(url_for('home'))

@login_required
@app.route('/db', methods=['GET', 'POST'])
def user_database():
    form = Del_form()
    if form.validate_on_submit():
        user = User.query.get(form.user_id.data)
        if user is None:
            flash('Non-exist user')
        elif user == current_user:
            flash('Cannot delete current user.')
        else:
            db.session.delete(user)
            db.session.commit()
    return render_template('db.html', form=form, data=User.query.all())

if __name__ == '__main__':
    app.run(debug=True)
