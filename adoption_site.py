#adoption_site.py
import os
from flask import Flask,render_template,redirect,url_for
from forms import AddForm,DelForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

######################sql database section ############### (can be done in mmodels.py )
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


##############models############
class Puppy(db.Model):
    """docstring for Puppy."""

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f" Puppy name is : {self.name} "


#############view functions ######### have forms ###takes user info saves it to the models

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add',methods=['GET','POST'])
def add_pupp():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pupp = Puppy(name)
        db.session.add(new_pupp)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    return render_template('add.html',form=form)

@app.route('/del',methods=['GET','POST'])
def delete_pupp():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_puppy'))

    return render_template('delete.html',form=form)



@app.route('/list')
def list_puppy():

    puppies = Puppy.query.all()  # retrn a list of all available puppies

    return render_template('list.html',puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)
