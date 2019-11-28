from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Addform(FlaskForm):
    name = StringField('Puppy Name')
    submit = SubmitField('Add Puppy')

class Delform(FlaskForm):
    id = IntegerField('Puupy ID')
    submit = SubmitField('Delete Puppy')
class Ownerform(FlaskForm):
    name = StringField('Owner Name')
    pup_id = IntegerField('Adopted puppy ID')
    submit = SubmitField('Add Owner')
