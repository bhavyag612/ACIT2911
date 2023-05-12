import pytest
from project.models import User
from project import create_app, db

@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def new_user(app):
    user = User(id=1,email='patkennedy79@gmail.com', password='FlaskIsAwesome',name='John')
    return user

@pytest.fixture
def populated_db(app, new_user):
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()