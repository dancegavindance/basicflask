from flask import request, Flask, Blueprint
from app.api_numpy.views import numpy
from app.api_intertools.views import intertools
from app.api_trigerhappy.views import trigerhappy

APP = Flask(__name__)
APP.register_blueprint(numpy)
APP.register_blueprint(intertools)
APP.register_blueprint(trigerhappy)




