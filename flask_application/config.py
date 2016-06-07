import logging
import os


class Config(object):
    def __init__(self):
        self.DEBUG = True
        self.TESTING = True
        self.SECRET_KEY = 'j34i5j345in3ingnaowitgf0pJENGU8273HNd'


app_config = Config()
