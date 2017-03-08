from flask import request, Flask, Blueprint
from app.api_numpy.views import numpy
from app.api_trigerhappy.views import trigerhappy
from app.api_itertools.views import itertools

APP = Flask(__name__)
APP.config["TRAP_HTTP_EXCEPTIONS"] = True
APP.register_blueprint(numpy)
APP.register_blueprint(trigerhappy)
APP.register_blueprint(itertools)



