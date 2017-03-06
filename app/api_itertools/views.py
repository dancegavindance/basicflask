from flask import Blueprint, request
import itertools as it
import json

itertools = Blueprint('itertools', __name__, url_prefix='/itertools')

@itertools.route('/')
@itertools.route('/index')
def index():

    return "testing"

@itertools.route('/product', methods=['POST'])
def cartesian_product():
	data = request.get_json()

	product = list(it.product(*data))

	return json.dumps(product)