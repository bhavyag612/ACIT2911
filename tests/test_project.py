from project.models import User
from project.database import db
def test_home(client):
    response=client.get("/")
    assert b'<title>Spondulix</title>' in response.data

def test_add_account_OK(client,app,new_user,populated_db):
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
        acc1=client.post(f"/{new_user.id}/addAccount",data={"account_name":"Scotia","initial_amount":100})
        acc2=client.post(f"/{new_user.id}/addAccount",data={"account_name":"Scotia"})

        user = User.query.filter_by(email=new_user.email).first()
        assert acc2.status_code==200
        assert len(user.accounts) == 2
        for account in user.accounts:
            assert account.amount >=0
        
def test_add_account_NOTOK(client,app,new_user,populated_db):
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
        acc=client.post(f"/{new_user.id}/addAccount",data={})

        user = User.query.filter_by(email=new_user.email).first()
        assert len(user.accounts) == 0
        assert acc.status_code==404
        assert b'Sorry there was an error' in acc.data

