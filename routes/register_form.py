from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(Form):
    email = StringField(validators=[DataRequired("Please enter email"), Email("Invalid email address")])
    firstname = StringField(validators=[DataRequired("First name is required")])
    lastname = StringField()
    password = PasswordField(validators=[DataRequired("Please enter password"),Length(min = 8),EqualTo('confirm',message="Passwords must match")])
    confirm = PasswordField()