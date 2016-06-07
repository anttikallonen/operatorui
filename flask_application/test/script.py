import sys
import nose
from flask_script import Command

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"


class RunTests(Command):
    """Runs the unittests"""

    def run(self, *args, **kwargs):
        nose.run(argv=[sys.argv[0]])
