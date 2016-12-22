from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(Form):
    email = StringField(validators=[DataRequired("Please enter email"), Email("Invalid email address")])
    firstname = StringField(validators=[DataRequired("First name is required")])
    lastname = StringField()
    password = PasswordField(validators=[DataRequired("Please enter password"),Length(min = 8,message="Password must be at least 8 characters long"),EqualTo('confirm',message="Passwords must match")])
    confirm = PasswordField()
    accept_toc = BooleanField(validators = [DataRequired("Without agreeing with the terms and conditions, you will be unable to register")])