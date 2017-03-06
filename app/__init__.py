from flask import Flask, Blueprint
from app.api_numpy.views import numpy
from app.api_intertools.views import intertools
from app.api_funky.views import funky

APP = Flask(__name__)
APP.register_blueprint(numpy)
APP.register_blueprint(intertools)
APP.register_blueprint(funky)




