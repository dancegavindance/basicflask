from flask import Blueprint, Response, request, url_for
from werkzeug.exceptions import HTTPException
import json
import numpy as np

CONTENT_TYPE = 'application/json'


numpy = Blueprint('numpy', __name__, url_prefix = '/numpy')


@numpy.errorhandler(HTTPException)
def handle_error(error):

	err_desc = {"error_description": error.description}
	return json.dumps(err_desc), error.status_code, CONTENT_TYPE

@numpy.route('/')
@numpy.route('/index')
def index():
	output = [{"name": "A range",
				"link": url_for("numpy.arange_call")},
						{"name": "from string",
						"link": url_for("numpy.fromstring_call")},
						{"name": "zeros",
						"link": url_for("numpy.zeros_call")},
						{"name": "ones",
						"link": url_for("numpy.ones_call")},
						{"name": "eye",
						"link": url_for("numpy.eye_call")}]
	return Response(json.dumps(output), status = 200, content_type = CONTENT_TYPE)


@numpy.route('/arange', methods=['POST'])
def arange_call():
	data = request.get_json()
	start = 0
	if "start" in data:
		start = data["start"]
	if "stop" in data:
		stop = data["stop"]
	if "step" in data:
		step = data["step"]
		if start is 0:
			return "you can't do that! If you define step you must also define start"
	output = np.arange(start, stop, step)
	return ', '.join([str(x) for x in output])

@numpy.route('/fromstring', methods=['POST'])
def fromstring_call():
	data = request.get_json()
	dtype = data["dtype"]
	string = data["str"]
	count = data["count"]
	sep = data["sep"]
	output = np.fromstring(string, dtype, count, sep)
	return ', '.join([str(x) for x in output])

@numpy.route('/zeros', methods=['POST'])
def zeros_call():
	data = request.get_json()
	shape = data["shape"]
	dtype = data["dtype"]
	output = np.zeros(shape, dtype)
	return ', '.join([str(x) for x in output])

@numpy.route('/ones', methods=['POST'])
def ones_call():
	data = request.get_json()
	shape = data["shape"]
	dtype = data["dtype"]
	output = np.ones(shape, dtype)
	return ', '.join([str(x) for x in output])

@numpy.route('/eye', methods=['POST'])
def eye_call():
	data = request.get_json()
	N = data["N"]
	M = data["M"]
	K = data["K"]
	dtype = data["dtype"]
	output = np.eye(N, M, K, dtype)
	return ', '.join([str(x) for x in output])
