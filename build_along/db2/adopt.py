import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import Addform, Delform, Ownerform
# config
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABC1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
# models
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner =   db.relationship('Owner', backref='pet', uselist=False)
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy ID:{self.id} - {self.name} is adpoted by {self.owner.name}'
        else:
            return f'Puppy ID:{self.id} - {self.name} has no owner yet.'

class Owner(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id
# view functions

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_pup', methods=['GET', 'POST'])
def add_pup():
    if Addform().validate_on_submit():
        name = Addform().name.data
        db.session.add(Puppy(name))
        db.session.commit()
        return redirect(url_for('data'))
    return render_template('add.html', form = Addform())

@app.route('/del',methods=['GET', 'POST'])
def delete():
    if Delform().validate_on_submit():
        pup = Puppy.query.get(Delform().id.data)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('data'))
    return render_template('del.html', form = Delform())

@app.route('/add_owner', methods=['GET','POST'])
def add_own():
    if Ownerform().validate_on_submit():
        name = Ownerform().name.data
        pup_id = Ownerform().pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('data'))
    return render_template('owner.html', form = Ownerform())

@app.route('/data')
def data():
    return render_template('data.html', list = Puppy.query.all())

if __name__ =='__main__':
    app.run(debug=True)
