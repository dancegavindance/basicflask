from flask import Flask, Blueprint
from app.api_numpy.views import numpy
APP = Flask(__name__)
APP.register_blueprint(numpy)
