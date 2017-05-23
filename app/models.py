from core import db

class bbranch(db.Model):
    bbranch_id = db.Column(db.Integer, primary_key=True)
    bbranch_name = db.Column(db.String(64), index=True, unique=True)
    bbranch_address = db.Column(db.String(64), index=True, unique=True)


class atm(db.Model):
    atm_id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, unique=True)
    atm_name = db.Column(db.String(64), index=True, unique=True)
    atm_address = db.Column(db.String(64), index=True, unique=True)
    cash_limit = db.Column(db.Integer, unique=True)
    
    
class transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, unique=True)
    atm_id = db.Column(db.Integer, unique=True)
    transaction_date = db.Column(db.String(64), unique=False)
    transaction_type_desc = db.Column(db.String(64), index=True, unique=True)
    transaction_amount = db.Column(db.Integer, unique=True)


class customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_firstname = db.Column(db.String(64), index=True, unique=True)
    customer_lastname = db.Column(db.String(64), index=True, unique=True)
    customer_lastname = db.Column(db.String(64), index=True, unique=True)

    
class account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, unique=True)
    account_type_id = db.Column(db.Integer, unique=True)
    amount = db.Column(db.Integer, unique=True)


class account_type(db.Model):
    account_type_id = db.Column(db.Integer, primary_key=True)
    account_type_desc = db.Column(db.String(64), index=True, unique=True)

   

class transaction_type(db.Model):
    transaction_type_id = db.Column(db.Integer, primary_key=True)
    transaction_type_desc = db.Column(db.String(64), index=True, unique=True)


class atm_card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, unique=True)

    
