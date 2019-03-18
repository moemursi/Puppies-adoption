#forms.py file
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):
    name = StringField("Name of the puppy :")
    submit = SubmitField("Add Puppy")

    pass

class DelForm(FlaskForm):
    id = IntegerField("Id number of the puppy to remove")
    submit =  SubmitField("Delete the Puppy")
