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
    users = dict()
    users["007"] = {"id": "007",
                    "name": "user1",
                    "consents": [{"id": "2323",
                                  "service1": "4134",
                                  "service2": "234234"}]}
    userdb.populate(users)


class TestUserRest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        populate_databases()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_currentuser_should_list_data_of_logged_user(self):
        with self.client:
            self.client.post("/api/auth/007")
            result = self.client.get("/api/currentuser")
            self.assertEquals(result.json["name"], "user1")

    def test_consents_should_list_consents_of_logged_user(self):
        with self.client:
            self.client.post("/api/auth/007")
            result = self.client.get("/api/currentuser/consents")
            self.assertEquals(len(result.json), 1)

    def test_post_consents_should_create_new_consent_for_logged_user(self):
        with self.client:
            self.client.post("/api/auth/007")
            self.client.post(
                '/api/currentuser/consents',
                data=json.dumps(dict(id="555", name="consent2")))
            result = self.client.get("/api/currentuser/consents")
            self.assertEquals(len(result.json), 2)
