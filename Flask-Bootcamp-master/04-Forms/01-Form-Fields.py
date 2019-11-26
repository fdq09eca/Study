from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):
    pass
    # '''
    # This general class gets a lot of form about puppies.
    # Mainly a way to go through many of the WTForms Fields.
    # '''
    # breed = StringField('What breed are you?',validators=[DataRequired()])
    # neutered  = BooleanField("Have you been neutered?")
    # mood = RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    # food_choice = SelectField(u'Pick Your Favorite Food:',
    #                       choices=[('chi', 'Chicken'), ('bf', 'Beef'),
    #                                ('fish', 'Fish')])
    # feedback = TextAreaField()
    # submit = SubmitField('Submit')

atts = ['breed', 'neutered', 'mood', 'food_choice', 'feedback', 'submit'] # the atts name can't be snake_case or cap. why??
att_types = [
StringField('What breed are you?',validators=[DataRequired()]),
BooleanField("Have you been neutered?"),
RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')]),
SelectField('Pick Your Favorite Food:',choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')]),
TextAreaField(),
SubmitField('Submit')
]

form_attrs = dict(zip(atts, att_types))
for att, att_type in form_attrs.items():
    setattr(InfoForm, att, att_type)
    # print(dir(getattr(InfoForm, att)))
    # if len(getattr(InfoForm, att).args)>0:
    #         print(att, getattr(InfoForm, att).args[0])


@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        for att in form_attrs.keys():
            session[att] = getattr(form, att).data
             # data attribute is available when form.validate_on_submit == True

        # Grab the data from the breed on the form.

        # session['breed'] = form.breed.data
        # session['neutered'] = form.neutered.data
        # session['mood'] = form.mood.data
        # session['food'] = form.food_choice.data
        # session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))


    return render_template('01-home.html', form=form, atts = form_attrs.keys())


@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html', atts = form_attrs.keys())


if __name__ == '__main__':
    app.run(debug=True)
