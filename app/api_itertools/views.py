from flask import Blueprint, Response, request, url_for
from werkzeug.exceptions import HTTPException
import itertools as it
import json

CONTENT_TYPE = 'application/json'

itertools = Blueprint('itertools', __name__, url_prefix='/itertools')

@itertools.errorhandler(HTTPException)
def handle_error(error):
	response = jsonify({'message': error.description['message']})

	return {'message': 'custom error message to appear in body'}, 404, CONTENT_TYPE

@itertools.route('/')
@itertools.route('/index')
def index():
	links = [
				{
					"name": "Product",
					"link": url_for("itertools.cartesian_product")
				},
				{
					"name": "Chain",
					"link": url_for("itertools.chain")
				},
				{
					"name": "izip",
					"link": url_for("itertools.izip")
				},
				{
					"name": "izip-longest",
					"link": url_for("itertools.izip_longest")
				},
				{
					"name": "Combinations",
					"link": url_for("itertools.combinations")
				}
			] 
	return Response(json.dumps(links), 200, content_type=CONTENT_TYPE) 

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

	combinations = list(it.combinations(data, r=2))

	return json.dumps(combinations)