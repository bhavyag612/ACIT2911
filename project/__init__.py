from flask import Flask
from pathlib import Path
from .database import db
from .routes import main
import json
from datetime import datetime, date

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)
def create_app(database_uri="sqlite:///budget.db"):
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    app.config['SECRET_KEY']='BudgetTrack'
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.instance_path = Path(".").resolve()
    db.init_app(app)

    #Creating the tables
    with app.app_context():
        db.create_all()
        print("All tables should have been created now.")
    app.register_blueprint(main)

    app.jinja_env.filters['json_decode'] = json_decode
    return app

def json_decode(data):
    return json.loads(data)

