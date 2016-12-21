from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(Form):
    email = StringField(validators=[DataRequired("Please enter email"), Email("Invalid email address")]) 
    password = PasswordField(validators=[DataRequired("Please enter password"),Length(min = 8)])#EqualTo('confirm',message="Passwords must match")
  