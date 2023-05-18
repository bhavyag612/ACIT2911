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

#API to add chart view
@main.route("/<int:account_id>/monthly_chart",methods=['GET'])
def monthly_chart(account_id):
    account=db.session.get(Account,account_id)
    data_dict=account.to_dict()
    return render_template('monthly_chart.html',account=(data_dict))
@main.route("/<int:user_id>/charts",methods=['GET'])
def user_chart(user_id):
    user=db.session.get(User,user_id)
    data_dict=user.to_dict() 
    return render_template('monthly_chart.html',account=(data_dict))


#API for Forecast expense and income
@main.route("/<int:account_id>/forecast",methods=['GET','POST'])
def monthly_forecast(account_id):
    if request.method =='POST':
        month=request.form.get('month')
    else:
        month=''
    account=db.session.get(Account,account_id)
    expense_dict={}
    income_dict={}
    new_exp_dict={}
    new_income_dict={}
    profitLoss=0
    for transaction in account.transactions:
        if month in transaction.trans_created.strftime("%Y-%m-%d"):
            if transaction.amt<0:
                if transaction.trans_created in expense_dict:
                    expense_dict[transaction.trans_created]+=transaction.amt
                else:
                    expense_dict[transaction.trans_created]=transaction.amt
            else:
                if transaction.trans_created in income_dict:
                    income_dict[transaction.trans_created]+=transaction.amt
                else:
                    income_dict[transaction.trans_created]=transaction.amt
    if len(expense_dict)>4:
        expense_list=list(expense_dict.values())
        running_avg=[]
        window=4
        for i in range(0,len(expense_dict)-window):
            subset= expense_list[i:i+window]
            avg=sum(subset)/window
            running_avg.append(avg)
        maxDate=(max(expense_dict.keys()))
        year=maxDate.year
        month=maxDate.month
        day=maxDate.day
        days_in_month = calendar.monthrange(year, month)[1]
        for i in range(day,days_in_month):
            maxDate+=timedelta(days=1)
            prediction=round((sum(expense_list[-(window-1):])+running_avg[-1])/window,2)
            expense_dict[maxDate]=prediction
            expense_list.append(prediction)
            subset= expense_list[-window:]
            avg=sum(subset)/window
            running_avg.append(avg)
        new_exp_dict = {}
        for key, value in expense_dict.items():
            new_key = key.strftime("%Y-%m-%d")
            new_exp_dict[new_key] = 0-value
        #######################################################
    if len(income_dict)>2:
        income_list=list(income_dict.values())
        income_keys=list(income_dict.keys())
        running_avg=[]
        window=2
        for i in range(0,len(income_dict)-window):
            subset= income_list[i:i+window]
            avg=sum(subset)/window
            running_avg.append(avg)
        maxDate=(max(income_dict.keys()))
        year=maxDate.year
        month=maxDate.month
        day=maxDate.day
        diff=0
        for i in range(0,len(income_dict)-1):
            diff+=(income_keys[i+1].day)-(income_keys[i].day)
        days_in_month = calendar.monthrange(year, month)[1]
        for i in range(day,days_in_month):
            maxDate+=timedelta(days=diff)
            if maxDate.month>month:
                break
            prediction=round((sum(income_list[-(window-1):])+running_avg[-1])/window,2)
            income_dict[maxDate]=prediction
            income_list.append(prediction)
            subset= income_list[-window:]
            avg=sum(subset)/window
            running_avg.append(avg)
        for i in range(0,len(expense_dict)-1):
            if (list(expense_dict.keys()))[i] in income_dict:
                continue
            else:
                income_dict[list(expense_dict.keys())[i]]=0
        sorted_income_dict = dict(sorted(income_dict.items(), key=lambda x: x[0]))
        new_income_dict = {}
        for key, value in sorted_income_dict.items():
            new_key = key.strftime("%Y-%m-%d")
            new_income_dict[new_key] = value
    profitLoss=round(sum(list(new_exp_dict.values()))-sum(list(new_income_dict.values())),2)
    return render_template('forecast.html',expense_dict=new_exp_dict,income_dict=new_income_dict,account_id=account.id,profitLoss=profitLoss)