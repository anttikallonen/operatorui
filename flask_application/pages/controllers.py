from flask import Blueprint
from flask import current_app, url_for
from flask_login import login_required
from flask import redirect

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"

pages = Blueprint('pages', __name__)


@pages.route('/')
def index():
    return redirect(url_for('pages.mainpage'))


@pages.route('/<path:filename>')
def staticfiles(filename):
    return redirect('static/' + filename)


@login_required
@pages.route('/mainpage')
def mainpage():
    return current_app.send_static_file('index.html')
