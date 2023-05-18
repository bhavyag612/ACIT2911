
from .database import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    name=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    accounts = db.relationship('Account', backref='user')
    def to_dict(self):
        transaction_list=[]
        for account in self.accounts:
            transaction_list+=[{"id":transaction.id,"amt":transaction.amt,"tag":transaction.tag,"date_created":transaction.trans_created}for transaction in account.transactions]
        user_dict={
            "id":self.id,
            "name":self.name,
            "transactions":transaction_list
        }
        return user_dict

    def __str__(self):
        return f'<User(id="{self.id}", email="{self.email}", name="{self.name}")>'

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    amount = db.Column(db.Float, default=0.0)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    transactions = db.relationship('Transaction', backref='account', cascade='all,delete')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    def to_dict(self):
        transaction_list=[{"amt":transaction.amt,"tag":transaction.tag,"date_created":transaction.trans_created}for transaction in self.transactions]
        account_dict={
            "id":self.id,
            "name":self.name,
            "amount":self.amount,
            "transactions":transaction_list
        }
        return account_dict
    def __str__(self):
        return f'<Account(id="{self.id}", name="{self.name}", amount="{self.amount}", date_added="{self.date_added}")>'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amt=db.Column(db.Float,nullable=False)
    tag=db.Column(db.String,nullable=False)
    comment=db.Column(db.String,nullable=True)
    trans_created=db.Column(db.Date, default=date.today())
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, index=True)

    def __str__(self):
        return f'<Transaction(id="{self.id}", amt="{self.amt}", tag="{self.tag}", comment="{self.comment}", trans_created="{self.trans_created}")>'
