from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed #profile picture upload
from flask_login import current_user
from blog.models import User

class Login_form(FlaskForm):
    email = StringField('Email ', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class Reg_form(FlaskForm):
    email = StringField('Email ', validators=[Email(), DataRequired()])
    username = StringField('Username ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_pw', message = 'Password must match.')])
    confirm_pw = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username has been registered')

class Update_User_form(FlaskForm):
    email = StringField('Email ', validators=[Email(), DataRequired()])
    username = StringField('Username ', validators=[DataRequired()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['png','jpg'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username has been registered')
