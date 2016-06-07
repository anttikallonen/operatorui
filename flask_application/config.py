import logging
import os

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


class Config(object):
    def __init__(self):
        self.DEBUG = True
        self.TESTING = True
        self.SECRET_KEY = 'j34i5j345in3ingnaowitgf0pJENGU8273HNd'


app_config = Config()
