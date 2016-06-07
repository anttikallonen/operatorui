from flask_application.database.memorydb import MemoryDatabase
from flask_login import login_user
from flask_application import login_manager


class UserDatabase(MemoryDatabase):
    def get_one(self, id):
        return User(super(UserDatabase, self).get_one(id))


class User():
    def __init__(self, data):
        self.data = data

    def get_id(self):
        return self.data['id']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


userdb = UserDatabase()


@login_manager.user_loader
def load_user(id):
    return userdb.get_one(id)
