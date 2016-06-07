from flask_application.database.memorydb import MemoryDatabase
from flask_login import login_user
from flask_application import login_manager

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


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
