from flask import Flask, Blueprint
from app.api_numpy.views import numpy
from app.api_itertools.views import itertools
from app.api_funky.views import funky

APP = Flask(__name__)
APP.config["TRAP_HTTP_EXCEPTIONS"] = True
APP.register_blueprint(numpy)
APP.register_blueprint(itertools)
APP.register_blueprint(funky)



