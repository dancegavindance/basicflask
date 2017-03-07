from flask import Blueprint, request
import math
import json

trigerhappy = Blueprint('trigerhappy', __name__, url_prefix = '/trigerhappy')

@trigerhappy.route('/')
@trigerhappy.route('/index')
def index():
    return "Tha trig page."

@trigerhappy.route('/sin', methods=['POST'])
def sin():

    rads = request.get_json()

    sine = math.sin(rads)

    return json.dumps(sine)


@trigerhappy.route('/cos', methods=['POST'])
def cos():
    rads = request.get_json()

    cosn = math.cos(rads)

    return json.dumps(cosn)


@trigerhappy.route('/tan', methods=['POST'])
def tan():
    rads = request.get_json()

    tant = math.tan(rads)

    return json.dumps(tant)




