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

if __name__ == "__main__":
    app.run(debug=True) #Starting the flask application