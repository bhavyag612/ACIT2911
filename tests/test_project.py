from project.models import User
from project.database import db
from flask_login import login_user
def test_home(client):
    response=client.get("/")
    assert b'<title>Spondulix</title>' in response.data

def test_add_account_OK(client,app,new_user,populated_db):
    with app.test_request_context():
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(email=new_user.email).first()
            login_user(user)
            with client.session_transaction() as session:
                session['_user_id'] = user.id
            client.set_cookie('localhost', 'user_id', str(new_user.id))
            acc1=client.post(f"/{new_user.id}/addAccount",data={"account_name":"Scotia","initial_amount":100})
            acc2=client.post(f"/{new_user.id}/addAccount",data={"account_name":"Scotia"})

            assert acc2.status_code==302
            assert len(user.accounts) == 2
            for account in user.accounts:
                assert account.amount >=0
        
def test_add_account_NOTOK(client,app,new_user,populated_db):
    with app.test_request_context():
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=new_user.email).first()
            login_user(user)
            with client.session_transaction() as session:
                session['_user_id'] = user.id
            acc=client.post(f"/{new_user.id}/addAccount",data={})

            assert len(user.accounts) == 0
            assert acc.status_code==404
            assert b'Sorry there was an error' in acc.data

