from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import Login_form, Reg_form

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    login_user()
    flash('You logged out.')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if Login_form().validate_on_submit():
        user = User.query.filter_by(email=Login_form().email.data).first()
        if user.check_password(Login_form().password.data) and user is not None:
            login_user(user)
            flash('Login successful.')
            next = request.args.get('next') # grab the page the user go next
            if next == None or not next[0]=='/': # if the user requested an invalid page, then request.args.get('next') == 0
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form=Login_form())

@app.route('/register', methods=['GET','POST'])
def register():
    if Reg_form().validate_on_submit():
        user = User(email=Reg_form().email.data, password=Reg_form().password.data, username=Reg_form().username.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registeration.')
        return redirect(url_for(login))
    return render_template('reg.html', form=Reg_form())

if __name__ == '__main__':
    app.run(debug='True')
