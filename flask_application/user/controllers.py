from flask import Blueprint
import flask_restful as restful
from flask_application.resources.protectedresource import ProtectedResource
from flask_application.mydata.mydatacontroller import mydatacontroller
from flask_login import current_user
from flask import redirect, url_for, current_app, request
from flask_login import logout_user
from flask import jsonify
import logging

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


class CurrentUserAPI(ProtectedResource):
    def get(self):
        return jsonify(current_user.data)


class ConsentAPI(ProtectedResource):
    def post(self):
        consentobject = request.get_json(force=True)
        mydatacontroller.set_consent_for_user(current_user.get_id(),
                                              consentobject)

    def get(self):
        return mydatacontroller.get_consents_for_user(current_user.get_id())


user = Blueprint('user', __name__)
api = restful.Api(user, prefix="/api")
api.add_resource(CurrentUserAPI, "/currentuser")
api.add_resource(ConsentAPI, "/currentuser/consents")
