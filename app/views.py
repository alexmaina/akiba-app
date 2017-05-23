##
#!/usr/bin/env python
from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')


@app.route('/login', methods = ['POST'])
def login():
    form = LoginForm()
   
    if request.method == 'POST':
      if form.validate() == False:
         flash('pin is required.')
         return render_template('login.html', form = form)
      else:
         return render_template('index.html')
    elif request.method == 'GET':
         return render_template('login.html', form = form)


@app.route('/withdrawCash', methods=['GET','POST'])
def withdrawCash():
         return render_template ('withdrawCash.html')


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


