from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import data_required, email, equal_to, length, ValidationError
from project.models import User

class Login_form(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": "you@example.com"}, validators=[data_required(), email()])
    # username = StringField('Username', render_kw={"placeholder": "yourusername"}, validators=[data_required()])
    password = PasswordField('Password', render_kw={"placeholder": "yourpassword"}, validators=[data_required()])
    submit = SubmitField('Login!')
    # def validate_submit(self, submit):
    #     user = User.query.filter_by(email = self.email.data).first()
    #     if user is None or user.check_password(self.passowrd.data) is False:
    #         raise ValidationError('Invalid email or passowrd')


class Reg_form(FlaskForm):
    email = StringField('Email', validators=[data_required(), email()], render_kw={"placeholder": "your@email.com"})
    username = StringField('Username', validators=[data_required()], render_kw={"placeholder": "Your username"})
    password = PasswordField('Password', validators=[data_required(), equal_to('confirm_pw', message='Password must match with the confirmed password.')], render_kw={"placeholder": "Your password"})
    confirm_pw = PasswordField('Confirm password', validators=[data_required()], render_kw={"placeholder": "Confirm your password"})
    submit = SubmitField('Register!')
    def validate_email(self, email):
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email has been registered')

    def validate_username(self, username):
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username has been registered')

class Del_form(FlaskForm):
    user_id = IntegerField('User Id', validators=[data_required()])
    submit = SubmitField('Delete User')
