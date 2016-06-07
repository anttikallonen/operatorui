from flask import Blueprint
import flask_restful as restful
from flask_application.resources.protectedresource import ProtectedResource
from flask_login import current_user
from flask import redirect, url_for, current_app, request
from flask_login import logout_user
from flask import jsonify
from flask_application.mydata.mydatacontroller import mydatacontroller
import logging

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


class ServiceAPI(ProtectedResource):
    def get(self, id):
        return mydatacontroller.get_service(id)

    def post(self):
        serviceobject = request.get_json(force=True)
        mydatacontroller.set_service(serviceobject)


class ServicesAPI(ProtectedResource):
    def get(self):
        return mydatacontroller.get_all_services()


service = Blueprint('service', __name__)
api = restful.Api(service, prefix="/api")

api.add_resource(ServiceAPI, "/service")
api.add_resource(ServicesAPI, "/services")
