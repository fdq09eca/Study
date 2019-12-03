from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError #Equalto is used for password confirmation

class Login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class Reg_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('password', message='Password must match!')])
    pass_confirm = PasswordField('Confirm_password', validators = [DataRequired()])
    submit = SubmitField('Register!')

def check_email(self, field):
    if User.query.filter_by(email=field.data).first():
        return ValidationError('Email has already been registered') # see https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
def check_user(self, field):
    if User.query.filter_by(username=field.data).first():
        return ValidationError('Username has already been registered') # see https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
