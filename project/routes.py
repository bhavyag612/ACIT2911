from pathlib import Path
from flask import Flask, jsonify, render_template, request, redirect,url_for,Blueprint
from .models import User,Account,Transaction
from datetime import datetime,timedelta
from .database import db
main = Blueprint("main", __name__)
import calendar
import json
#API call for index_page
@main.route("/")
def home():
    return render_template("login.html")

#API to show the user homepage after clicking the login button
@main.route("/<int:user_id>",methods=["GET"])
def user_main_page(user_id):
    user=User.query.get(user_id)
    total_amount=0
    for account in user.accounts:
        total_amount+=account.amount
    return render_template('transactions_home.html',user=user,total_amount=total_amount)

#API to show transactions of individual accounts
@main.route("/<int:user_id>/<int:account_id>",methods=["GET"])
def user_account(user_id,account_id):
    user=User.query.get(user_id)
    return render_template('user_account.html',user=user,accountReq=account_id)

#API to add an account
@main.route("/<int:user_id>/addAccount",methods=['GET','POST'])
def add_account(user_id):
    try:
        if request.method=='GET':
            return render_template('add_account.html',user_id=user_id)
        else:
            user=db.session.get(User,user_id)
            account_name=(request.form.get('account_name'))  
            initial_amount=(request.form.get('initial_amount'))
            if account_name:
                if initial_amount:
                    account=Account(name=account_name,amount=initial_amount,user_id=user.id)
                else:
                    account=Account(name=account_name,user_id=user.id)
            else:
                raise ValueError
            db.session.add(account)
            db.session.commit()
            return redirect(url_for('main.user_main_page',user_id=user_id)),200
    except:
        return 'Sorry there was an error',404

#API to Delete Account
@main.route('/<int:account_id>/delete',methods=['POST'])
def delete_account(account_id):
    account=Account.query.get(account_id)
    user_id=account.user_id
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('main.user_main_page',user_id=user_id))

#API to Add transaction
@main.route("/<int:account_id>/addTansaction",methods=['POST','GET'])
def add_transaction(account_id):
    account=Account.query.get(account_id)
    user=User.query.get(account.user_id)
    if request.method=='GET':
        return render_template('add_transaction.html',account_id=account_id,user_id=user.id)
    else:
        toggle=(request.form.get('toggle'))
        amount=round(float(request.form.get('amount')),2)
        tag=(request.form.get('category'))
        comment=(request.form.get('comment'))
        date=datetime.strptime((request.form.get('date')), '%Y-%m-%d').date()
        
        if toggle=='income':
            transaction=Transaction(amt=amount,tag=tag,comment=comment,trans_created=date,account_id=account_id)
        else:
            transaction=Transaction(amt=-amount,tag=tag,comment=comment,trans_created=date,account_id=account_id)
        account.amount+=transaction.amt
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('main.user_main_page',user_id=user.id))

#API to view a transaction
@main.route('/<int:transaction_id>/view',methods=['GET'])
def view_transaction(transaction_id):
    transaction=Transaction.query.get(transaction_id)
    account=Account.query.get(transaction.account_id)
    user=User.query.get(account.user_id)
    return render_template('view_transaction.html',transaction=transaction,user_id=user.id)

#API to delete a transaction
@main.route("/<int:transaction_id>/delTansaction",methods=['POST'])
def delete_transaction(transaction_id):
    transaction=Transaction.query.get(transaction_id)
    account=Account.query.get(transaction.account_id)
    user=User.query.get(account.user_id)
    account.amount -= transaction.amt
    db.session.delete(transaction)
    db.session.commit()
    return render_template("user_account.html",user=user,accountReq=account.id)

#API to update transaction
@main.route("/<int:transaction_id>/update",methods=['POST','GET'])
def update_transaction(transaction_id):
    transaction=Transaction.query.get(transaction_id)
    account=Account.query.get(transaction.account_id)
    user=User.query.get(account.user_id)
    if request.method=='GET':
        return render_template('update_transaction.html',transaction=transaction,user_id=user.id)
    else:
        toggle=(request.form.get('toggle'))
        amount=round(float(request.form.get('amount')),2)
        tag=(request.form.get('category'))
        comment=(request.form.get('comment'))
        date=datetime.strptime((request.form.get('date')), '%Y-%m-%d').date()
        account.amount-=transaction.amt
        transaction.tag=tag
        transaction.comment=comment
        transaction.trans_created=date
        if toggle=='income':
            transaction.amt=amount
        else:
            transaction.amt=0-(amount)
        account.amount+=transaction.amt
        db.session.commit()
        return redirect(url_for('main.user_main_page',user_id=user.id))

