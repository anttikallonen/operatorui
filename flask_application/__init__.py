import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from flask_login import LoginManager
from flask import redirect
import logging

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,
            template_folder=os.path.join(FLASK_APP_DIR, '..', 'templates'),
            static_folder=os.path.join(FLASK_APP_DIR, '..', 'static'))

# Config
app.config.from_object('flask_application.config.app_config')

# Login
login_manager = LoginManager()
login_manager.init_app(app)

# Logging
app.logger.setLevel(logging.INFO)

# Business Logic
# http://flask.pocoo.org/docs/patterns/packages/
# http://flask.pocoo.org/docs/blueprints/
from flask_application.auth.controllers import auth
app.register_blueprint(auth)
from flask_application.user.controllers import user
app.register_blueprint(user)
from flask_application.service.controllers import service
app.register_blueprint(service)
from flask_application.pages.controllers import pages
app.register_blueprint(pages)
