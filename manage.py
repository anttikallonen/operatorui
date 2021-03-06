#!/usr/bin/env python
from flask_script import Manager
from flask_script.commands import Server, Shell, ShowUrls, Clean

from flask_application import app
from flask_application.test.script import RunTests

__author__ = "Antti Kallonen"
__copyright__ = "Copyright 2016, Tampere University of Technology"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "antti.kallonen@tut.fi"

manager = Manager(app)
manager.add_command("run_server",
                    Server(host="0.0.0.0",
                           port=9000,
                           use_reloader=True))
manager.add_command("show_urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command('run_tests', RunTests())

if __name__ == "__main__":
    manager.run()
