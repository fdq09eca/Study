# adpotion_site.py
import os
from form import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '123344ff'

## SQL DB SECTION
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

## MODELS
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Puppy name: {self.name}'

## view function -- have forms
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    if AddForm().validate_on_submit():
        name = AddForm().name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=AddForm())

@app.route('/list')
def list_pup():
    data = Puppy.query.all()
    return render_template('list.html', data = data)

@app.route('/del', methods=['GET', 'POST'])
def del_pup():
    if DelForm().validate_on_submit():
        id = DelForm().id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('del.html', form=DelForm())
if __name__ == '__main__':
    app.run(debug=True)
