from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    card_id = StringField('card_id', validators=[DataRequired("Please enter card id")])
    pin = PasswordField('pin', validators=[DataRequired("please enter pin")])
    submit = SubmitField('Enter >>')

class RegistrationForm(Form):
    card_id = StringField('card_id', validators=[DataRequired("Please enter card id")])
    pin = PasswordField('pin', validators=[DataRequired("please enter pin")])
    account_id = IntegerField('account_id', validators=[DataRequired("please enter account id")])
    submit = SubmitField('Enter >>')
    

class WithdrawCash(Form):
    amount = StringField('amount', validators=[DataRequired("Please enter amount")])
    submit = SubmitField('Enter >>')

