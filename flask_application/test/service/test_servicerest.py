import logging
import json
from flask_testing import TestCase
from flask_application import app
from flask_application.config import app_config
from flask_application.user.models import userdb
from flask_application.service.models import servicedb

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


def populate_databases():
    services = dict()
    services["1234"] = {"name": "service1",
                        "labels": ["food"],
                        "linkurl": "http://mydatalink.com/service1"}
    services["1235"] = {"name": "service2",
                        "labels": ["food"],
                        "linkurl": "http://mydatalink.com/service2"}
    servicedb.populate(services)


class TestServiceRest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        populate_databases()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_get_all_services_should_return_correct_number_of_services(self):
        with self.client:
            result = self.client.get("/api/services")
            self.assertEqual(len(result.json), 2)

    def test_set_service_should_add_new_service_to_collection(self):
        with self.client:
            self.client.post(
                '/api/service',
                data=json.dumps(dict(id="555", name="service3")))
            result = self.client.get("/api/services")
            self.assertEqual(len(result.json), 3)
