from flask import Flask
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
from .auth import load_user
from pathlib import Path
from .database import db
from .routes import main
import json
from datetime import datetime, date


def create_app(database_uri="sqlite:///budget.db"):
    app = Flask(__name__)
    app.config['SECRET_KEY']='BudgetTrack'
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.instance_path = Path(".").resolve()
    db.init_app(app)

    #Creating the tables
    with app.app_context():
        db.create_all()
        print("All tables should have been created now.")
    app.register_blueprint(main)

    # Flask Login Setup
    login_manager = LoginManager()
    login_manager.login_view = "/login"
    login_manager.login_message = "You Must Login to Access This Page!"
    login_manager.login_message_category = "danger"
    login_manager.init_app(app)

    # Set the user loader callback
    login_manager.user_loader(load_user)
    return app

def json_decode(data):
    return json.loads(data)

