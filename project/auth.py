from .models import User
def load_user(id):
    return User.query.get(int(id))
