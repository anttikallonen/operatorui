from flask_application.service.models import servicedb
from flask_application.user.models import userdb
from flask_login import login_user, logout_user


class MyDataController():
    def login_user(self, userid):
        # TODO Connect to MyData Account
        login_user(userdb.get_one(userid))

    def set_consent_for_user(self, userid, consentobject):
        # TODO Connect to consenting
        userdb.get_one(userid).data['consents'].append(consentobject)

    def get_consents_for_user(self, userid):
        # TODO Connect to consenting
        return userdb.get_one(userid).data['consents']

    def get_user(self, userid):
        # TODO Connect to user database
        return userdb.get_one(userid)

    def get_service(self, id):
        # TODO Connect to Service Registry
        servicedb.get_one(id)

    def set_service(self, serviceobject):
        # TODO Connect to Service Registry
        servicedb.set_one(serviceobject['id'], serviceobject)

    def get_all_services(self):
        # TODO Connect to Service Registry
        return servicedb.get_all()


mydatacontroller = MyDataController()
