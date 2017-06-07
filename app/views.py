##
#!/usr/bin/env python
from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm
from .forms import RegistrationForm
from .forms import WithdrawCash
import sqlite3 as sql
from bcrypt import hashpw, gensalt, checkpw
import bcrypt


@app.route('/')
@app.route('/index')


##login
@app.route('/login', methods = ['POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate() == True:
      
         #return render_template('index.html')
         card_id = request.form['card_id']
         pin = request.form['pin']
         con = sql.connect("testDB.db")
         cur = con.cursor()
         cur.execute("SELECT pin FROM atm_card where card_id =?", (card_id,))
         hashed = cur.fetchone()

         if hashed is None or not checkpw(pin, hashed[0]):
              return "user not found"
         else:
	      print (card_id)
              return render_template('index.html')
    
    else:
        return render_template('login.html', form = form)


##withdraw cash
@app.route('/withdrawCash', methods=['GET','POST'])
def withdrawCash():
         form = WithdrawCash()
         #return render_template ('withdrawCash.html', form = form)
         if request.method == 'POST' and form.validate() == True:
            amount = request.form['amount']
            return 'you have successfully withdrawn ' + amount +  '&nbsp' + 'shillings' 
         else:
             return render_template ('withdrawCash.html', form = form)
         


@app.route('/confirmWithdrawal', methods=['GET','POST'])
def confirmWithdrawal():
         return render_template ('confirmWithdrawal.html')

@app.route('/completeCashWithdrawal', methods=['GET', 'POST'])
def completeCashWithdrawal():
     return render_template ('completeCashWithdrawal.html')


@app.route('/cashTransfer', methods=['GET', 'POST'])
def cashTransfer():
     return render_template ('cashTransfer.html')


@app.route('/transferMpesa', methods=['GET', 'POST'])
def transferMpesa():
     return render_template ('transferMpesa.html')


@app.route('/checkBalance', methods=['GET', 'POST'])
def checkBalance():
     return render_template ('checkBalance.html')


@app.route('/currentAccountBalance', methods=['GET', 'POST'])
def currentAccountBalance():
     return render_template ('currentAccountBalance.html')


@app.route('/savingsAccountBalance', methods=['GET', 'POST'])
def savingsAccountBalance():
     return render_template ('savingsAccountBalance.html')

         
    
     

   

