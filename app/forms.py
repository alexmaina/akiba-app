from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    pin = PasswordField('pin', validators=[DataRequired()])
    

class withdrawalCash(Form):
    amount = StringField('amount', validators=[DataRequired()])
