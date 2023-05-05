from pathlib import Path
from flask import Flask, jsonify, render_template, request, redirect,url_for
from models import User,Account,Transaction
from datetime import datetime
from database import db
app = Flask(__name__)
app.config['SECRET_KEY']='BudgetTrack'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///budget.db"
app.instance_path = Path(".").resolve()
db.init_app(app)

#Creating the tables
with app.app_context():
    db.create_all()
    print("All tables should have been created now.")

#API call for index_page
@app.route("/")
def home():
    return render_template("login.html")

#API to show the user homepage after clicking the login button
@app.route("/<int:user_id>",methods=["GET"])
def user_main_page(user_id):
    user=User.query.get(user_id)
    total_amount=0
    for account in user.accounts:
        total_amount+=account.amount
    return render_template('transactions_home.html',user=user,total_amount=total_amount)

if __name__ == "__main__":
    app.run(debug=True) #Starting the flask application