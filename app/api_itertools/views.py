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

@itertools.route('/chain', methods=['POST'])
def chain():
	data = request.get_json()

	chain = list(it.chain(*data))

	return json.dumps(chain)

@itertools.route('/izip', methods=['POST'])
def izip():
	data = request.get_json()

	izip = list(it.izip(*data))

	return json.dumps(izip)

@itertools.route('/izip-longest', methods=['POST'])
def izip_longest():
	data = request.get_json()

	izip_longest = list(it.izip_longest(*data, fillvalue='-'))

	return json.dumps(izip_longest)

@itertools.route('/combinations', methods=['POST'])
def combinations():
	data = request.get_json()

	combinations = list(it.combinations(*data, r=2))

	return json.dumps(combinations)