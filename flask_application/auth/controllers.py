from flask import Blueprint
import flask_restful as restful
from flask_application.resources.protectedresource import ProtectedResource
from flask_login import current_user
from flask import redirect, url_for, current_app
from flask_login import login_user, logout_user
from flask import jsonify
from flask_application.user.models import User
import logging
from flask_application.mydata.mydatacontroller import mydatacontroller


class AuthAPI(ProtectedResource):
    def post(self, id):
        mydatacontroller.login_user(id)


auth = Blueprint('auth', __name__)
api = restful.Api(auth, prefix="/api")

api.add_resource(AuthAPI, "/auth/<string:id>")
